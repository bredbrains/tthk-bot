import json
import os

import requests

from models.change import Change
from models.consultation import Consultation

api_url = os.environ["api"]


class API:
    def __init__(self):
        self.api_url = api_url

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

    def get_consultations_by_teacher(self, teacher):
        r = requests.get(self.api_url + 'consultations')
        consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        consultations = []
        for item in consultations_json:
            consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                        item["times"])
            if teacher in consultation.teacher:
                consultations.append(consultation.get_str())
        if consultations:
            return consultations
        return None

    def get_groups(self):
        r = requests.get(self.api_url + 'groups')
        groups_json = eval(json.dumps(r.json()))["data"]
        groups = []
        for item in groups_json:
            groups.append(item["group"])
        if groups:
            return groups
        return None

    def get_teachers(self):
        r = requests.get(self.api_url + 'teachers')
        teachers_json = eval(json.dumps(r.json()))["data"]
        if teachers_json:
            return teachers_json
        return None
