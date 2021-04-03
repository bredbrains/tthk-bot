import json

import requests

import os

from models.change import Change
from models.consultation import Consultation


class API:
    def __init__(self):
        self.api_url = os.environ["api"]

    def get_changes(self):
        r = requests.get(self.api_url + 'changes')
        changes_json = eval(json.dumps(r.json()))["data"]
        changes = []
        for item in changes_json:
            change = Change(item["dayofweek"], item["date"], item["group"], item["lessons"], item["teacher"],
                            item["room"])
            changes.append(change.get_str())
        if changes:
            return changes
        return None

    def get_changes_by_group(self, group):
        r = requests.get(self.api_url + 'changes')
        changes_json = eval(json.dumps(r.json()))["data"]
        changes = []
        for item in changes_json:
            change = Change(item["dayofweek"], item["date"], item["group"], item["lessons"], item["teacher"],
                            item["room"])
            if group in change.group:
                changes.append(change)
        if changes:
            return changes
        return None

    def get_consultations(self):
        r = requests.get(self.api_url + 'consultations')
        consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
                consultations.append(consultation.get_str())
        if consultations:
            return consultations
        return None

    def get_consultations_by_teacher(self, teacher):
        r = requests.get(self.api_url + 'consultations')
        consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
                if teacher in consultation.teacher:
                    consultations.append(consultation.get_str())
        if consultations:
            return consultations
        return None

    def get_consultations_by_department(self, department):
        r = requests.get(self.api_url + 'consultations?department=' + department)
        consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
                consultations.append(consultation.get_str())
        if consultations:
            return consultations
        return None

    def search_teachers(self):
        r = requests.get(self.api_url + 'consultations')
        consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
                consultations.append(consultation.get_teacher())
        if consultations:
            return consultations
        return None

    def search_departments(self):
        r = requests.get(self.api_url + 'consultations')
        consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
                consultations.append(consultation.get_department())
        if consultations:
            return consultations
        return None
