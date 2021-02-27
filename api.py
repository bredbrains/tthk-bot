from models.change import Change
from models.consultation import Consultation
import json

import requests

class API:
    def __init__(self):
        self.api_url = "http://bredbrains.tech/api/"

    def get_changes(self):
        r = requests.get(self.api_url + 'changes')
        changes_json = eval(json.dumps(r.json()))["data"]
        changes = []
        for item in changes_json:
            change = Change(item["dayofweek"], item["date"], item["group"], item["lessons"], item["teacher"],
                            item["room"])
            changes.append(change.get_str())
        if changes:
            return '\n'.join(changes)
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
            return '\n'.join(changes)
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
            return '\n'.join(consultations)
        return None
