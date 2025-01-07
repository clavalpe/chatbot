from dataclasses import dataclass
import logging
from abc import ABC, abstractmethod
from typing import Dict, Sequence
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage, BaseMessage, trim_messages
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    language: str


class AIClient(ABC):
    @abstractmethod
    def invoke(self, conversation_id: str, message: str) -> None: ...


class OpenAIClientError(Exception): ...


class LangChainClient(AIClient):
    MODEL = "gpt-4o-mini"

    def __init__(self) -> None:
        workflow: StateGraph = StateGraph(state_schema=MessagesState)

        # Define the (single) node in the graph
        workflow.add_edge(START, "model")
        workflow.add_node("model", self._call_model)

        # Add memory
        self._compiled_workflow = workflow.compile(checkpointer=MemorySaver())

    def _call_model(self, state: State) -> Dict[str, list]:
        model = ChatOpenAI(model=self.MODEL, temperature=0)

        trimmer = trim_messages(
            max_tokens=65,
            strategy="last",
            token_counter=model,
            include_system=True,
            allow_partial=False,
            start_on="human",
        )
        trimmed_messages = trimmer.invoke(state["messages"])

        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful assistant.",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        prompt = prompt_template.invoke({"messages": trimmed_messages})

        response = model.invoke(prompt)
        return {"messages": response}

    def invoke(self, conversation_id: str, message: str) -> str:
        input_messages = [HumanMessage(message)]
        config = {"configurable": {"thread_id": conversation_id}}
        logging.info(f"Sending request to chatbot. Message: '{input_messages}'")
        try:
            chat_output = self._invoke_chat(config, input_messages)
        except Exception as e:
            logging.error(f"Error invoking AI client: {e}")
            raise OpenAIClientError

        logging.info("Chatbot response received.")
        return chat_output["messages"][-1].content

    def _invoke_chat(self, config, input_messages):
        response = self._compiled_workflow.invoke(
            {"messages": input_messages}, config=config
        )
        return response


@dataclass
class Conversation:
    user: str
    ai_client: AIClient

    def call(self, message: str) -> str:
        conversation_id = self.user
        return self.ai_client.invoke(conversation_id, message)


class ConversationRepository(ABC):
    @abstractmethod
    def get(self, user: str) -> Conversation: ...


class InMemoryConversationRepository(ConversationRepository):
    def __init__(self) -> None:
        self._conversations: list[Conversation] = []

    def get(self, user: str) -> Conversation:
        for conversation in self._conversations:
            if conversation.user == user:
                return conversation

        new_conversation = Conversation(user=user, ai_client=LangChainClient())
        self._conversations.append(new_conversation)

        return new_conversation


class SendMessage:
    def __init__(self, conversation_repository: ConversationRepository) -> None:
        self._conversation_repository = conversation_repository

    def execute(self, user: str, message: str) -> str:
        conversation = self._conversation_repository.get(user)

        ai_response = conversation.call(message=message)

        return ai_response
