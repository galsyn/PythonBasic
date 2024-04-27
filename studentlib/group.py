from .exception import *

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise MyException(f'{student.first_name} {student.last_name}', "Запис в групу завершено")
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        for student in self.group:
            if last_name == student.last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f'{student.first_name} {student.last_name}, '
        return f'Number:{self.number}\n {all_students} '.strip(" ").strip(",")
