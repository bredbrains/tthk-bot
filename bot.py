import asyncio
from typing import Optional

import vkbottle.bot as bot
from vkbottle.bot import Message

from api import API
from models.group import Group
from userskeyboard import UsersKeyboard


class Bot:
    def __init__(self, token):
        self.bot = bot.Bot(token)
        self.api = API()
        self.keyboard = UsersKeyboard()

        self.group_choosing = False

        @self.bot.on.private_message(text=["Изменения в расписании"])
        async def any_message(message: Message):
            await message.answer('Изменения в расписании', keyboard=self.keyboard.get_group_keyboard())

        @self.bot.on.private_message(text=["Все группы",
                                           "Моя группа"])
        async def any_message(message: Message):
            group = self.keyboard.group
            changes = None
            await message.answer("Подождите пожалуйста пару секунд...")
            if group is not None:
                try:
                    changes = self.api.get_changes_by_group(group)
                except:
                    await message.answer("Похоже на то, что сайт TTHK временно не функционирует,\n"
                                         "либо был изменен и на данный момент не поддерживается.")
            else:
                try:
                    changes = self.api.get_changes()
                except:
                    await message.answer("Похоже на то, что сайт TTHK временно не функционирует,\n"
                                         "либо был изменен и на данный момент не поддерживается.")
            if changes:
                try:
                    await message.answer(changes)
                except:
                    await message.answer(changes[900:])
            elif group:
                await message.answer("Для группы, которую вы указали изменений в расписании нет.")
            else:
                await message.answer("Изменений в расписании нет.")

        @self.bot.on.private_message(text=["Консультации"])
        async def any_message(message: Message, teacher: Optional[str] = None):
            consultation = None
            await message.answer("Подождите пожалуйста 5 секунд...")
            if teacher is not None:
                try:
                    consultation = self.api.get_consultations_by_teacher(teacher)
                except:
                    await message.answer("Похоже на то, что сайт TTHK временно не функционирует,\n"
                                         "либо был изменен и на данный момент не поддерживается.")
            else:
                try:
                    consultation = self.api.get_consultations_by_teacher(teacher)
                except:
                    await message.answer("Похоже на то, что сайт TTHK временно не функционирует,\n"
                                         "либо был изменен и на данный момент не поддерживается.")
            if consultation:
                await message.answer(consultation)
            elif teacher:
                await message.answer("Нет такого учителя, которого вы указали.")
            else:
                await message.answer("Нет данных о консультациях.")

        @self.bot.on.private_message(text=["Выбрать группу"])
        async def any_message(message: Message):
            self.group_choosing = True
            await message.answer('Выберите аббревиатуру Вашей группы',
                                 keyboard=self.keyboard.get_group_professions_keyboard())

        @self.bot.on.private_message(text=Group.get_professions())
        async def any_message(message: Message):
            if self.group_choosing:
                await message.answer('Выберите градацию Вашей группы',
                                     keyboard=self.keyboard.get_group_graduation_keyboard())

        @self.bot.on.private_message(text=Group.get_graduations())
        async def any_message(message: Message):
            if self.group_choosing:
                await message.answer('Выберите год Вашей группы',
                                     keyboard=self.keyboard.get_group_years_keyboard())

        @self.bot.on.private_message(text=Group.get_years())
        async def any_message(message: Message):
            if self.group_choosing:
                await message.answer('Выберите номер Вашей группы',
                                     keyboard=self.keyboard.get_group_number_keyboard())

        @self.bot.on.private_message(text=Group.get_numbers())
        async def any_message(message: Message):
            if self.group_choosing:
                await message.answer('Ваша группа',
                                     keyboard=self.keyboard.get_group_keyboard())

        @self.bot.on.private_message(text=["Консультации"])
        async def any_message(message: Message):
            await message.answer('Консультации', keyboard=self.keyboard.get_consultation_keyboard())

        @self.bot.on.private_message(text=["Консультации"])
        async def any_message(message: Message):
            await message.answer('Консультации', keyboard=self.keyboard.get_consultation_keyboard())

        @self.bot.on.private_message(text=["Назад"])
        async def any_message(message: Message):
            await message.answer('Назад', keyboard=self.keyboard.get_main_keyboard())

        @self.bot.on.private_message(text=["Начать",
                                           "Start"])
        async def wrapper(message: Message):
            await message.answer('Ваша клавиатура', keyboard=self.keyboard.get_main_keyboard())

        asyncio.run(self.bot.run_polling())
