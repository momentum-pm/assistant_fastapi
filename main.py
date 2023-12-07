from fastapi_poe import make_app
from modal import Image, Stub, asgi_app
from .bot import MainBot

image = Image.debian_slim().pip_install_from_requirements("requirements.txt")
stub = Stub("poe-server-bot-quick-start")
bot = MainBot()


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    app = make_app(bot, allow_without_key=True)
    return app
