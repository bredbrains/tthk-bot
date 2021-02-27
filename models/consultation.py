class ConsultationTemplate:
    @staticmethod
    def convert(consultation):
        return f"Учитель {consultation.teacher} \nКабинет: {consultation.room}\nПочта: {consultation.email}" \
               f"\nОтрасль: {consultation.department} " \
               f"\nДень недели: {consultation.weekday}\n Время: {consultation.time}\n"


class Consultation:
    def __init__(self, teacher, room, email, department, times, weekday, time):
        self.teacher = teacher
        self.room = room
        self.email = email
        self.department = department
        self.times = times
        self.weekday = weekday
        self.time = time

    def get_str(self) -> str:
        return ConsultationTemplate.convert(self)
