from models.change import Change
from models.consultation import Consultation
import json

import requests

class API:
    def __init__(self):

        # --------------------------------------------------------------------------------------------------------------------
        #                                         Url getting
        # --------------------------------------------------------------------------------------------------------------------

        self.api_url = "http://bredbrains.tech/api/"

    # --------------------------------------------------------------------------------------------------------------------
    #                                         Changes
    # --------------------------------------------------------------------------------------------------------------------

    def get_changes(self):
        r = requests.get(self.api_url + 'changes')
        try:
            changes_json = eval(json.dumps(r.json()))["data"]
        except:
            return None
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
        try:
            changes_json = eval(json.dumps(r.json()))["data"]
        except:
            return None
        changes = []
        for item in changes_json:
            change = Change(item["dayofweek"], item["date"], item["group"], item["lessons"], item["teacher"],
                            item["room"])
            if group in change.group:
                changes.append(change.get_str())
        if changes:
            return '\n'.join(changes)
        return None

    # --------------------------------------------------------------------------------------------------------------------
    #                                         Consultations
    # --------------------------------------------------------------------------------------------------------------------

    def get_consultations(self):
        r = requests.get(self.api_url + 'consultations')
        try:
            consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        except:
            return None
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
            consultations.append(consultation.get_str())
        if consultations:
            return '\n'.join(consultations)
        return None

    def get_consultations_by_teacher(self, teacher):
        r = requests.get(self.api_url + 'consultations')
        try:
            consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        except:
            return None
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
            if teacher in consultation.teacher:
                consultations.append(consultation.get_str())
        if consultations:
            return '\n'.join(consultations)
        return None

    def get_consultations_by_department(self, department):
        r = requests.get(self.api_url + 'consultations?department='+department)
        try:
            consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        except:
            return None
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
            consultations.append(consultation.get_str())
        if consultations:
            return '\n'.join(consultations)
        return None

    # --------------------------------------------------------------------------------------------------------------------
    #                                         Teacher searching
    # --------------------------------------------------------------------------------------------------------------------

    def search_teachers(self):
        r = requests.get(self.api_url + 'consultations')
        try:
            consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        except:
            return None
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
            consultations.append(consultation.get_teachers())
        if consultations:
            return '\n'.join(consultations)
        return None

    def search_teacher_by_name(self, name):
        r = requests.get(self.api_url + 'consultations')
        try:
            consultations_json = eval(json.dumps(r.json()).replace("null", "None"))["data"]
        except:
            return None
        consultations = []
        for item in consultations_json:
            for temporal in item["times"]:
                consultation = Consultation(item["teacher"], item["room"], item["email"], item["department"],
                                            item["times"], temporal["weekday"], temporal["time"])
            if name in consultation.teacher:
                consultations.append("я нашел учителя : " + consultation.get_teachers())
        if consultations:
            return '\n'.join(consultations)
        return None