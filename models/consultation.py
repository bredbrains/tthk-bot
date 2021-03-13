class ConsultationTemplate:
    @staticmethod
    def convert(consultation):
        return f"👨‍🏫 Учитель {consultation.teacher} \nКабинет: {consultation.room}\n✉ Почта: {consultation.email}" \
               f"\nОтрасль: {consultation.department} " \
               f"\n🗓 День недели: {consultation.weekday}\n⏰ Время: {consultation.time}\n"


class TeacherSearchingTemplate:
    @staticmethod
    def convert(consultation):
        return f"{consultation.teacher}"


class DepartmentSearchingTemplate:
    @staticmethod
    def convert(consultation):
        return f"{consultation.department}"


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

    def get_teacher(self) -> str:
        return TeacherSearchingTemplate.convert(self)

    def get_department(self) -> str:
        return TeacherSearchingTemplate.convert(self)
