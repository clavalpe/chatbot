from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage


class ChatOpenAIClient:
    def __init__(self):
        self._open_ai_chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def invoke(self, message: str) -> str:
        msg = HumanMessage(content=message, name="Lance")

        messages = [msg]
        chat_output = self._invoke_chat(messages)

        return chat_output.content

    def _invoke_chat(self, messages: list[HumanMessage]) -> AIMessage:
        return self._open_ai_chat.invoke(messages)
