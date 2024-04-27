from .human import *


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}\ngender: {self.gender}\nage: {self.age}\n'

    def find_student(self, name, group):
        if not group.find_student(name):
            return None
        return self.__str__()
