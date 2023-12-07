from typing import AsyncIterable
from fastapi_poe import PoeBot
from fastapi_poe.types import PartialResponse, QueryRequest
from .llm import LLM


class MainBot(PoeBot):
    def __init__(self):
        self.llm = LLM()

    async def get_response(
        self, request: QueryRequest
    ) -> AsyncIterable[PartialResponse]:
        messages = []
        for message in request.query:
            messages.append(message.content)
        last_message = messages.pop()
        response_text = self.llm.process(last_message)
        yield PartialResponse(text=response_text)
