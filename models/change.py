from enum import Enum


class ChangeTypes(Enum):
    Replacement = 1
    Removed = 2
    Lunch = 3
    IndependentWorkAtHome = 4
    IndependentWork = 5


class ChangeTemplate:
    def __init__(self, change):
        self.change = change


class Change:
    def __init__(self, dayofweek, date, group, lessons, teacher, room):
        self.dayofweek = dayofweek
        self.date = date
        self.group = group
        self.lessons = lessons
        self.teacher = teacher
        self.room = room
        self.type = self.get_type()

    def get_type(self) -> ChangeTypes:
        never_happen = "jääb ära"
        lunch_break = "söögivahetund"
        independent_work = "iseseisev töö"
        independent_work_at_home = "iseseisev töö kodus"
        if self.change.lesson in never_happen or self.change.teacher in never_happen:
            return ChangeTypes.Removed
        elif self.change.teacher in independent_work_at_home or self.change.teacher in independent_work_at_home:
            return ChangeTypes.IndependentWorkAtHome
        elif self.change.teacher in independent_work or self.change.room in independent_work:
            return ChangeTypes.IndependentWork
        elif self.change.teacher in lunch_break or self.change.teacher in lunch_break:
            return ChangeTypes.Ind
        return ChangeTypes.Replacement
