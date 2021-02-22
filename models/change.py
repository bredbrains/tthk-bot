from enum import Enum


class ChangeTypes(Enum):
    Replacement = 1
    Removed = 2
    Lunch = 3
    IndependentWorkAtHome = 4
    IndependentWork = 5


class ChangeTemplate:
    @staticmethod
    def convert(change):
        change.type = change.get_type()
        change_date = ""
        if change.type == ChangeTypes.Removed:
            return change_date + f"🗓 {change.dayofweek} Дата: {change.date}\n🦆 Группа: {change.group} ⏰ Урок: {change.lessons} \n❌ Не состоится\n"
        elif change.type == ChangeTypes.IndependentWorkAtHome:
            return change_date + f"🗓 {change.dayofweek} Дата: {change.date}\n🦆 Группа: {change.group} ⏰ Урок: {change.lessons} \n🏠 Самостоятельная работа дома\n"
        elif change.type == ChangeTypes.IndependentWork:
            return change_date + f"🗓 {change.dayofweek} Дата: {change.date}\n🦆 Группа: {change.group} ⏰ Урок: {change.lessons} \n👨‍🏫 Преподаватель: {change.teacher}\nКабинет: {change.room}\n"
        elif change.type == ChangeTypes.Lunch:
            return change_date + f"🗓 {change.dayofweek} Дата: {change.date}\n🦆 Группа: {change.group} ⏰ Урок: {change.lessons} \n🆒 Обеденный перерыв\n"
        return change_date + f"🗓 {change.dayofweek} Дата: {change.date}\n🦆 Группа: {change.group} ⏰ Урок: {change.lessons} \n👨‍🏫 Преподаватель: {change.teacher}\nКабинет: {change.room}\n"


class Change:
    def __init__(self, dayofweek, date, group, lessons, teacher, room):
        self.dayofweek = dayofweek
        self.date = date
        self.group = group
        self.lessons = lessons
        self.teacher = teacher
        self.room = room

    def get_type(self) -> ChangeTypes:
        never_happen = "jääb ära"
        lunch_break = "söögivahetund"
        independent_work = "iseseisev töö"
        independent_work_at_home = "iseseisev töö kodus"
        if self.lessons in never_happen or self.teacher in never_happen:
            return ChangeTypes.Removed
        elif self.teacher in independent_work_at_home or self.teacher in independent_work_at_home:
            return ChangeTypes.IndependentWorkAtHome
        elif self.teacher in independent_work or self.room in independent_work:
            return ChangeTypes.IndependentWork
        elif self.teacher in lunch_break or self.teacher in lunch_break:
            return ChangeTypes.Lunch
        return ChangeTypes.Replacement

    def get_str(self) -> str:
        return ChangeTemplate.convert(self)
