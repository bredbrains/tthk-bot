from vkbottle import Keyboard, KeyboardButtonColor, Text

from models.group import Group


class UsersKeyboard:

    def __init__(self):
        self.keyboard = None
        self.group_abbreviation = None
        self.group_graduation = None
        self.group_years = None
        self.group = None
        self.row_empty = None

    def get_main_keyboard(self):
        self.keyboard = Keyboard(one_time=False) \
            .add(Text("Изменения в расписании"), color=KeyboardButtonColor.POSITIVE) \
            .row() \
            .add(Text("Консультации"), color=KeyboardButtonColor.POSITIVE) \
            .get_json()
        return self.keyboard

    def get_consultation_keyboard(self):
        self.keyboard = Keyboard(one_time=False) \
            .add(Text("Мой список"), color=KeyboardButtonColor.PRIMARY) \
            .add(Text("Учителя по отрослям"), color=KeyboardButtonColor.PRIMARY) \
            .row() \
            .add(Text("Добавить учителя"), color=KeyboardButtonColor.SECONDARY) \
            .add(Text("Удалить учителя"), color=KeyboardButtonColor.SECONDARY) \
            .row() \
            .add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE) \
            .get_json()
        return self.keyboard

    def get_group_keyboard(self):
        self.keyboard = Keyboard(one_time=False) \
            .add(Text("Моя группа"), color=KeyboardButtonColor.PRIMARY) \
            .add(Text("Все группы"), color=KeyboardButtonColor.PRIMARY) \
            .row() \
            .add(Text("Выбрать группу"), color=KeyboardButtonColor.SECONDARY) \
            .row() \
            .add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE) \
            .get_json()
        return self.keyboard

    def get_group_professions_keyboard(self):
        self.keyboard = Keyboard(one_time=False)
        tick = 0
        for el in Group.get_professions():
            tick += 1
            self.keyboard.add(Text(el), color=KeyboardButtonColor.SECONDARY)
            self.row_empty = False
            if tick % 4 == 0:
                self.keyboard.row()
                self.row_empty = True
        if not self.row_empty:
            self.keyboard.row()
        self.keyboard.add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
        return self.keyboard.get_json()

    def get_group_graduation_keyboard(self):
        self.keyboard = Keyboard(one_time=False)
        tick = 0
        for el in Group.get_graduations():
            tick += 1
            self.keyboard.add(Text(el), color=KeyboardButtonColor.SECONDARY)
            self.row_empty = False
            if tick % 4 == 0:
                self.keyboard.row()
                self.row_empty = True
        if not self.row_empty:
            self.keyboard.row()
        self.keyboard.add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
        return self.keyboard.get_json()

    def get_group_years_keyboard(self):
        self.keyboard = Keyboard(one_time=False)
        tick = 0
        for el in Group.get_years():
            tick += 1
            self.keyboard.add(Text(el), color=KeyboardButtonColor.SECONDARY)
            self.row_empty = False
            if tick % 4 == 0:
                self.keyboard.row()
                self.row_empty = True
        if not self.row_empty:
            self.keyboard.row()
        self.keyboard.add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
        return self.keyboard.get_json()

    def get_group_number_keyboard(self):
        self.keyboard = Keyboard(one_time=False)
        tick = 0
        for el in Group.get_numbers():
            tick += 1
            self.keyboard.add(Text(el), color=KeyboardButtonColor.SECONDARY)
            self.row_empty = False
            if tick % 4 == 0:
                self.keyboard.row()
                self.row_empty = True
        if not self.row_empty:
            self.keyboard.row()
        self.keyboard.add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
        return self.keyboard.get_json()
