import asyncio

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

        self.group = None
        self.page = 0
        self.state = None

        print("Готово")

        @self.bot.on.private_message(text=["Изменения в расписании"])
        async def wrapper(message: Message):
            self.state = "group"
            if self.group is None:
                await message.answer("Выберите группу",
                                     keyboard=self.keyboard.get_separated_keyboard_by_array(self.groups, self.page))
            else:
                await message.answer(self.get_changes_by_group(self.group),
                                 keyboard=self.keyboard.get_main())

        @self.bot.on.private_message(text=self.groups)
        async def wrapper(message: Message):
            await message.answer(self.get_changes_by_group(message.text),
                                 keyboard=self.keyboard.get_main())

        @self.bot.on.private_message(text=self.teachers)
        async def wrapper(message: Message):
            teacher = message.text
            consultations = self.api.get_consultations_by_teacher(teacher)
            if consultations is not None:
                await message.answer(consultations)
            else:
                await message.answer("У данного учителя нет консультации")

        @self.bot.on.private_message(text=["⇦", "⇨"])
        async def wrapper(message: Message):
            if message.text == "⇦":
                if self.page > 0:
                    self.page -= 1
            elif message.text == "⇨":
                if self.page < len(self.groups) // 24:
                    self.page += 1
            if self.state == "group":
                await message.answer("Выберите группу",
                                     keyboard=self.keyboard.get_separated_keyboard_by_array(self.groups, self.page))

        @self.bot.on.private_message(text=["Назад"])
        async def wrapper(message: Message):
            await message.answer('Выберите команду', keyboard=self.keyboard.get_main())

        @self.bot.on.private_message(text=["Начать",
                                           "Start"])
        async def wrapper(message: Message):
            await message.answer('Ваша клавиатура', keyboard=self.keyboard.get_main())

        asyncio.run(self.bot.run_polling())

    def get_changes_by_group(self, group):
        if self.group is not None:
            changes = self.api.get_changes_by_group(group)
            if changes is not None:
                return changes
            else:
                return "Нет изменений в расписании"
        else:
            self.group = group
            return "Ваша группа " + self.group
