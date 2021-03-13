import json
from datetime import datetime
from enum import Enum


class GroupData(Enum):
    Professions = 1
    Graduations = 2
    Numbers = 3


class Group:
    def __init__(self, profession, graduation, year, number):
        self.profession = profession
        self.graduation = graduation
        self.year = year
        self.number = number

    def __str__(self):
        if self.number:
            return self.profession + self.graduation + self.year + "-" + self.number
        return self.profession + self.graduation + self.year

    @staticmethod
    def read_file():
        file = open("assets/group.json", "r", encoding="utf-8")
        data = json.load(file)
        file.close()
        return data

    @staticmethod
    def select_from_file(selection: GroupData):
        data = Group.read_file()
        selections = {
            GroupData.Professions: "professions",
            GroupData.Graduations: "graduations",
            GroupData.Numbers: "numbers"
        }
        return data[selections[selection]]

    @staticmethod
    def get_professions():
        return Group.select_from_file(GroupData.Professions)

    @staticmethod
    def get_graduations():
        return Group.select_from_file(GroupData.Graduations)

    @staticmethod
    def get_numbers():
        return Group.select_from_file(GroupData.Numbers)

    @staticmethod
    def get_years():
        group_years = []
        coly = 0
        if datetime.today() < datetime(datetime.today().year, 8, 31):
            coly = 1
        for tick in range(coly, 3 + coly):
            group_years.append(str(datetime.today().year - 2000 - tick))
        return group_years
