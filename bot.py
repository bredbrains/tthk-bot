import vkbottle.bot as bot
from vkbottle.bot import Message
import asyncio


class Bot:
    def __init__(self, token):
        self.bot = bot.Bot(token)

        @self.bot.on.message()
        async def any_message(message: Message):
            await message.answer("something")

        asyncio.run(self.bot.run_polling())

