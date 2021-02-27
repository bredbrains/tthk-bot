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
            .add(Text("изменения в расписании"), color=KeyboardButtonColor.POSITIVE) \
            .add(Text("консультации"), color=KeyboardButtonColor.POSITIVE) \
            .row() \
            .add(Text("список учителей"), color=KeyboardButtonColor.POSITIVE) \
            .add(Text("список команд"), color=KeyboardButtonColor.POSITIVE) \
            .row() \
            .add(Text("убрать клавиатуру"), color=KeyboardButtonColor.NEGATIVE) \
            .get_json()

        self.clearboard = Keyboard(one_time=True, inline=False) \
            .get_json()

        @self.bot.on.chat_message(text=[])
        @self.bot.on.private_message(text=["изменения в расписании для <group>",
                                           "изменения для <group>",
                                           "замены для <group>",
                                           "замены у <group>" 
                                           "замены",
                                           "изменения в расписании",
                                           "изменения"])
        async def any_message(message: Message, group: Optional[str] = None):
            if group is not None:
                changes = self.api.get_changes_by_group(group)
            else:
                changes = self.api.get_changes()
            if changes:
                try:
                    await message.answer(changes)
                except:
                    await message.answer(changes[900:])
            elif group:
                await message.answer("для группы, которую вы указали изменений в расписании нет.")
            else:
                await message.answer("изменений в расписании нет.")

        @self.bot.on.chat_message(text=[])
        @self.bot.on.private_message(text=["консультации у <teacher>",
                                           "консультации"])
        async def any_message(message: Message, teacher: Optional[str] = None):
            if teacher is not None:
                consultation = self.api.get_consultations_by_teacher(teacher)
            else:
                consultation = self.api.get_consultations()
            if consultation:
                try:
                    await message.answer(consultation)
                except:
                    await message.answer(consultation[:900])
            elif teacher:
                await message.answer("нет такого учителя, которого вы указали.")
            else:
                await message.answer("нет данных о консультациях.")

        @self.bot.on.chat_message(text=[])
        @self.bot.on.private_message(text=["список учителей",
                                           "учителя",
                                           "поиск учителя <teacher>",
                                           "поиск <teacher>",
                                           "учитель <teacher>"])
        async def any_message(message: Message, teacher: Optional[str] = None):
            if teacher is not None:
                search = self.api.search_teacher_by_name(teacher)
            else:
                search = self.api.search_teachers()
            if search:
                try:
                    await message.answer(search)
                except:
                    await message.answer(search[:900])
            elif teacher:
                await message.answer("нет такого учителя, которого вы указали.")
            else:
                await message.answer("нет данных об учителях.")

        @self.bot.on.chat_message(text=[])
        @self.bot.on.private_message(text=["список команд",
                                           "команды"])
        async def wrapper(message: Message):
            await message.answer('Пишем группы и учителей без <> **\n\n'
                                 'Изменения в расписании *\n'
                                 'изменения в расписании для <группа>, \n'
                                 'изменения для <группа>, \n'
                                 'замены для <группа>, \n'
                                 'замены у <группа>, \n'
                                 'замены, \n'
                                 'изменения в расписании, \n'
                                 'изменения\n\n'
                                 'Консультации *\n'
                                 'консультации, \n'
                                 'консультации у <учитель>\n\n'
                                 'Клавиатура *\n'
                                 'Вызов клавиатуры : '
                                 'привет, '
                                 'хай, '
                                 'здраствуй, '
                                 'клавиатура, '
                                 'клава \n'
                                 'Убрать клавиатуру : '
                                 'пока, '
                                 'уйди, '
                                 'убрать клавиатуру, '
                                 'убрать\n\n'
                                 'Другие комманды *\n'
                                 'Получить список учителей : '
                                 'список учителей, '
                                 'учителя\n'
                                 'Поиск учителя : '
                                 'поиск <учитель>, '
                                 'поиск учителя <учитель>, '
                                 'учитель <учитель>')

        @self.bot.on.chat_message(text=[])
        @self.bot.on.private_message(text=["привет",
                                           "хай",
                                           "здравствуй",
                                           "клавиатура",
                                           "клава"])
        async def wrapper(message: Message):
            await message.answer('ваша клавиатура', keyboard=self.keyboard)

        @self.bot.on.chat_message(text=[])
        @self.bot.on.private_message(text=["убрать клавиатуру",
                                           "убрать",
                                           "пока",
                                           "уйди"])
        async def wrapper(message: Message):
            await message.answer('клавиатура убрана', keyboard=self.clearboard)

        asyncio.run(self.bot.run_polling())

