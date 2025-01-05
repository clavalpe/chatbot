from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.graph.state import CompiledStateGraph
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from typing import Dict


# class ChatOpenAIClient:
#     def __init__(self):
#         self._open_ai_chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)

#     def invoke(self, message: str) -> str:
#         msg = HumanMessage(content=message, name="Lance")

#         messages = [msg]
#         chat_output = self._invoke_chat(messages)

#         return chat_output.content

#     def _invoke_chat(self, messages: list[HumanMessage]) -> AIMessage:
#         return self._open_ai_chat.invoke(messages)


class ChatOpenAIClient:
    def __init__(self):
        self.model: ChatOpenAI = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.workflow: StateGraph = StateGraph(state_schema=MessagesState)
        self.config: Dict = {"configurable": {"thread_id": "abc123"}}
        self.memory: MemorySaver = MemorySaver()

    def invoke(self, compiled_workflow: CompiledStateGraph, message: str) -> str:
        input_messages = [HumanMessage(message)]
        chat_output = self._invoke_chat(compiled_workflow, input_messages)
        return chat_output["messages"][-1].content

    def build_workflow(self) -> CompiledStateGraph:
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self._call_model)
        compiled_workflow = self.workflow.compile(checkpointer=self.memory)
        return compiled_workflow

    def _call_model(self, state: MessagesState) -> Dict[str, list]:
        response = self.model.invoke(state["messages"])
        return {"messages": response}

    def _invoke_chat(self, compiled_workflow, input_messages):
        output = compiled_workflow.invoke({"messages": input_messages}, self.config)
        return output
