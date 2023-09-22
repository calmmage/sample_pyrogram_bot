from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pyrogram import Client, filters
import asyncio

# step 1: pydantic config -
load_dotenv()
class AppSettings(BaseSettings):
    api_id: int
    api_hash: str
    bot_token: str

app_settings = AppSettings()

app = Client("test_app_name", api_id=app_settings.api_id,
             api_hash=app_settings.api_hash)

async def run_bot():
    pass

async def run_cli():
    pass

async def main(cli=False):
    if cli:
        await asyncio.gather(run_cli(), run_bot())
        # q: is this the right way to do it?
        # a:
        # to use asyncio.gather with functions a() and b()
        # you need to call them like this:
        # await asyncio.gather(a(), b())
        # if you call them like this:
        # await asyncio.gather(a, b)
        # it will not work
        # q: can I pass a list?
        # a: yes, you can pass a list of coroutines
        # await asyncio.gather(*[a(), b()])

    else:
        await run_bot()

