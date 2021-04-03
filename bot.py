import asyncio
from typing import Optional

import vkbottle.bot as bot
from vkbottle.bot import Message

from api import API
from userskeyboard import UsersKeyboard


class Bot:
    def __init__(self, token):
        self.bot = bot.Bot(token)
        self.api = API()
        self.keyboard = UsersKeyboard()
        self.groups = self.api.get_groups()
        self.teachers = self.api.get_teachers()

        print("Готово")

        @self.bot.on.private_message(text=self.groups)
        async def wrapper(message: Message):
            group = message.text
            changes = self.api.get_changes_by_group(group)
            if changes is not None:
                await message.answer(changes)
            else:
                await message.answer("Нет изменений в расписании")

        @self.bot.on.private_message(text=self.teachers)
        async def wrapper(message: Message):
            teacher = message.text
            consultations = self.api.get_consultations_by_teacher(teacher)
            if consultations is not None:
                await message.answer(consultations)
            else:
                await message.answer("Нет изменений в расписании")

        @self.bot.on.private_message(text=["Начать",
                                           "Start"])
        async def wrapper(message: Message):
            await message.answer('Ваша клавиатура', keyboard=self.keyboard.get_main())

        asyncio.run(self.bot.run_polling())
