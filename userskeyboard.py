from vkbottle import Keyboard, KeyboardButtonColor, Text
from api import API


class UsersKeyboard:

    def __init__(self):
        self.keyboard = None
        self.api = API()
        self.buttons_limiter = 8
        self.last_row = False

    def get_main(self):
        self.keyboard = Keyboard(one_time=False) \
            .add(Text("Изменения в расписании"), color=KeyboardButtonColor.POSITIVE) \
            .row() \
            .add(Text("Консультации"), color=KeyboardButtonColor.POSITIVE) \
            .get_json()
        return self.keyboard

    def get_separated_keyboard_by_array(self, array, page):
        self.keyboard = Keyboard(one_time=False)
        tick = 1
        for el in array[page * self.buttons_limiter:self.buttons_limiter * (page + 1)]:
            self.keyboard.add(Text(el), color=KeyboardButtonColor.PRIMARY)
            if tick % 4:
                self.keyboard.row()
            tick += 1

        self.keyboard.add(Text("<"), color=KeyboardButtonColor.SECONDARY)
        self.keyboard.add(Text(">"), color=KeyboardButtonColor.SECONDARY)
        self.keyboard.row()
        self.keyboard.add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
        self.keyboard.get_json()
        return self.keyboard
