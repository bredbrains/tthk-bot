import vkbottle.bot as bot
from vkbottle.bot import Message
from vkbottle import Keyboard, Text, KeyboardButtonColor
import asyncio
from api import API
from typing import Optional

class Bot:
    def __init__(self, token):
        self.bot = bot.Bot(token)
        self.api = API()

        self.keyboard = Keyboard(one_time=False, inline=False) \
            .add(Text("замены"), color=KeyboardButtonColor.POSITIVE) \
            .add(Text("консультации"), color=KeyboardButtonColor.POSITIVE) \
            .row() \
            .add(Text("убрать клавиатуру"), color=KeyboardButtonColor.NEGATIVE) \
            .get_json()

        self.clearboard = Keyboard(one_time=True, inline=False) \
            .get_json()

        @self.bot.on.chat_message(text=["-thk?changes <param>"])
        @self.bot.on.private_message(text=["изменения в расписании <param>", "замены <param>"])
        async def any_message(message: Message, param: Optional[str] = None):
            if param is not None:
                changes = self.api.get_changes_by_group(param)
            else:
                changes = self.api.get_changes()
            if changes:
                await message.answer(changes)
            await message.answer("для группы, которую вы указали изменений в расписании нет.")

        @self.bot.on.chat_message(text=["-thk?consutltations <teacher>"])
        @self.bot.on.private_message(text=["консультации <teacher>"])
        async def any_message(message: Message):
            changes = self.api.get_consultations()
            await message.answer(changes)

        @self.bot.on.chat_message(text=["-thk?привет", "-thk?хай", "-thk?здравствуй", "-thk?команды", "-thk?клавиатура", "-thk?клава"])
        @self.bot.on.private_message(text=["привет", "хай", "здравствуй", "команды", "клавиатура", "клава"])
        async def wrapper(message: Message):
            await message.answer('список команд', keyboard=self.keyboard)

        @self.bot.on.chat_message(text=["-thk?убрать клавиатуру", "-thk?убрать"])
        @self.bot.on.private_message(text=["убрать клавиатуру", "убрать"])
        async def wrapper(message: Message):
            await message.answer('клавиатура убрана', keyboard=self.clearboard)

        asyncio.run(self.bot.run_polling())

