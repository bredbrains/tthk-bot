from vkbottle import Keyboard, KeyboardButtonColor, Text
from api import API


class UsersKeyboard:

    def __init__(self):
        self.keyboard = None
        self.api = API()
        self.buttons_limiter = 24
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
        tick = 0
        min_count = page * self.buttons_limiter
        max_count = (page + 1) * self.buttons_limiter
        for el in array[min_count:max_count]:
            tick += 1
            self.keyboard.add(Text(el), color=KeyboardButtonColor.PRIMARY)
            self.last_row = False
            if tick % 3 == 0:
                self.keyboard.row()
                self.last_row = True
        if not self.last_row:
            self.keyboard.row()
        self.keyboard.add(Text("⇦"), color=KeyboardButtonColor.SECONDARY)
        self.keyboard.add(Text("⇨"), color=KeyboardButtonColor.SECONDARY)
        self.keyboard.row()
        self.keyboard.add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
        self.keyboard.get_json()
        return self.keyboard
