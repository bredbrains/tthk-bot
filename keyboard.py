from vkbottle import Keyboard, KeyboardButtonColor, Text
from datetime import datetime
from api import API


class Keyboard:

    def __init__(self):
        self.keyboard = None
        self.group_abbreviation = None
        self.group_graduation = None
        self.group_years = None
        self.group_number = None
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

    def get_abbreviation(self):
        self.group_abbreviation = [
            "AUM", "AUT", "KRR", "LOGA",
            "LOGIT", "MEH", "MRA", "SKA",
            "TAR", "TIT", "ROO", "BRB",
            "JKS", "VLOG", "AKT", "ATM",
            "EKS", "FRE", "KYM", "LMT",
            "MÜK", "ROT", "SAD", "NÜR",
            "STÕ"
        ]
        return self.group_abbreviation

    def get_graduation(self):
        self.group_graduation = [
            "pe", "pv",
            "ge", "gv",
            "geMS", "gvMS",
            "geÕ", "gvÕ"
        ]
        return self.group_graduation

    def get_year(self):
        self.group_years = []
        coly = 0
        if datetime.today() < datetime(datetime.today().year, 8, 31):
            coly = 1
        for tick in range(coly, 3 + coly):
            self.group_years.append(str(datetime.today().year - 2000 - tick))
        return self.group_years

    def get_number(self):
        self.group_number = [
            "1", "2", "Нету"
        ]
        return self.group_number

    def get_group_abbreviation_keyboard(self):
        self.keyboard = Keyboard(one_time=False)
        tick = 0
        for el in self.get_abbreviation():
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
        for el in self.group_graduation:
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
        for el in self.group_years:
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
        for el in self.group_number:
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
