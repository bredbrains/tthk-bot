import asyncio
from typing import Optional

import vkbottle.bot as bot
from vkbottle import Keyboard, Text, KeyboardButtonColor
from vkbottle.bot import Message

from api import API


class Bot:
    def __init__(self, token):
        self.bot = bot.Bot(token)
        self.api = API()

        self.keyboard = Keyboard(one_time=False, inline=False) \
            .add(Text("изменения в расписании"), color=KeyboardButtonColor.POSITIVE) \
            .row() \
            .add(Text("список учителей"), color=KeyboardButtonColor.POSITIVE) \
            .row() \
            .add(Text("убрать клавиатуру"), color=KeyboardButtonColor.NEGATIVE) \
            .get_json()

        self.clearboard = Keyboard(one_time=True, inline=False) \
            .get_json()

        @self.bot.on.chat_message(text=["-thk?изменения в расписании для <group>",
                                        "-thk?изменения для <group>",
                                        "-thk?замены для <group>",
                                        "-thk?замены у <group>"
                                        "-thk?замены",
                                        "-thk?изменения в расписании",
                                        "-thk?изменения"])
        @self.bot.on.private_message(text=["изменения в расписании для <group>",
                                           "изменения для <group>",
                                           "замены для <group>",
                                           "замены у <group>"
                                           "замены",
                                           "изменения в расписании",
                                           "изменения"])
        async def any_message(message: Message, group: Optional[str] = None):
            await message.answer("подождите пожалуйста пару секунд...")
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

        @self.bot.on.chat_message(text=["-thk?консультации у <teacher>",
                                        "-thk?консультации"])
        @self.bot.on.private_message(text=["консультации у <teacher>",
                                           "консультации"])
        async def any_message(message: Message, teacher: Optional[str] = None):
            await message.answer("подождите пожалуйста 5 секунд...")
            if teacher is not None:
                consultation = self.api.get_consultations_by_teacher(teacher)
            else:
                consultation = self.api.get_consultations()
            if consultation:
                try:
                    await message.answer(consultation)
                except:
                    await message.answer(
                        consultation[:800] + "\n\nсоветую смотреть консультации у конкретного учителя.")
            elif teacher:
                await message.answer("нет такого учителя, которого вы указали.")
            else:
                await message.answer("нет данных о консультациях.")

        @self.bot.on.chat_message(text=[])
        @self.bot.on.private_message(text=["привет",
                                           "хай",
                                           "здравствуй",
                                           "клавиатура",
                                           "клава"])
        async def wrapper(message: Message):
            await message.answer('х', keyboard=self.keyboard)

        asyncio.run(self.bot.run_polling())
