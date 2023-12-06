from fastapi_poe import make_app
from typing import AsyncIterable
from fastapi_poe import PoeBot
from fastapi_poe.types import PartialResponse, QueryRequest
from modal import Image, Stub, asgi_app

# from llm import LLM


class TestBot(PoeBot):
    def __init__(self):
        # self.chat_model = LLM(openai_api_key=OPENAI_API_KEY)
        pass

    async def get_response(
        self, request: QueryRequest
    ) -> AsyncIterable[PartialResponse]:
        messages = []
        # for message in request.query:
        #     if message.role == "bot":
        #         messages.append(AIMessage(content=message.content))
        #     elif message.role == "system":
        #         messages.append(SystemMessage(content=message.content))
        #     elif message.role == "user":
        #         messages.append(HumanMessage(content=message.content))

        response = self.chat_model.predict_messages(messages).content
        yield PartialResponse(text="salam")


image = Image.debian_slim().pip_install_from_requirements("requirements.txt")
stub = Stub("poe-server-bot-quick-start")
bot = TestBot()


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    app = make_app(bot, allow_without_key=True)
    return app
