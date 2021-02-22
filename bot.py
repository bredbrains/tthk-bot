import vkbottle.bot as bot
from vkbottle.bot import Message
import asyncio
from api import API
from typing import Optional

class Bot:
    def __init__(self, token):
        self.bot = bot.Bot(token)
        self.api = API()

        @self.bot.on.chat_message(text=["-thk?changes <param>"])
        @self.bot.on.private_message(text=["изменения в расписании <param>", "замены <param>"])
        async def any_message(message: Message, param: Optional[str] = None):
            if param is not None:
                changes = self.api.get_changes_by_group(param)
            else:
                changes = self.api.get_changes()
            if changes:
                await message.answer(changes)
            await message.answer("Для группы, которую вы указали изменений в расписании нет.")

        @self.bot.on.chat_message(text=["-thk?consutltations <teacher>"])
        @self.bot.on.private_message(text=["консультации <teacher>"])
        async def any_message(message: Message):
            changes = self.api.get_consultations()
            await message.answer(changes)

        asyncio.run(self.bot.run_polling())

