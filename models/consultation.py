class ConsultationTemplate:
    @staticmethod
    def convert(consultation):
        times = ""
        for temporal in consultation.times:
            times += "\n🗓 Консультация: " + temporal["weekday"] + " ⏰ Время: " + temporal["time"]
        return f"👨‍🏫 Учитель: {consultation.teacher}\n🚪 Кабинет: {consultation.room}\n✉ Почта: {consultation.email}" \
               f"\n⚒ Отрасль: {consultation.department}" \
               f"{times}\n"


class TeacherSearchingTemplate:
    @staticmethod
    def convert(consultation):
        return f"{consultation.teacher}"


class DepartmentSearchingTemplate:
    @staticmethod
    def convert(consultation):
        return f"{consultation.department}"


class Consultation:
    def __init__(self, teacher, room, email, department, times):
        self.teacher = teacher
        self.room = room
        self.email = email
        self.department = department
        self.times = times

    def get_str(self) -> str:
        return ConsultationTemplate.convert(self)

    def get_teacher(self) -> str:
        return TeacherSearchingTemplate.convert(self)

    def get_department(self) -> str:
        return TeacherSearchingTemplate.convert(self)
