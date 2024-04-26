class MyException(Exception):

    def __init__(self, x, message):
        super().__init__()
        self.message = message
        self.x = x

    def get_message(self):
        return self.message


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'Human: {self.first_name} {self.last_name}\ngender: {self.gender}\nage: {self:age}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}\ngender: {self.gender}\nage: {self.age}\n'


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
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f'{student.first_name} {student.last_name}, '
        return f'Number:{self.number}\n {all_students} '.strip(" ").strip(",")


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 25, 'John', 'Clark', 'AN143')
st4 = Student('Female', 23, 'Melissa', 'Fair', 'AN146')
st5 = Student('Male', 32, 'Alex', 'Frogg', 'AN141')
st6 = Student('Female', 30, 'Helen', 'Saylor', 'AN147')
st7 = Student('Male', 26, 'Bob', 'Berkly', 'AN148')
st8 = Student('Female', 28, 'Luisa', 'Minelle', 'AN144')
st9 = Student('Male', 31, 'Emanuil', 'Kant', 'AN140')
st10 = Student('Female', 28, 'Sirin', 'Shubert', 'AN150')
st11 = Student('Male', 25, 'Joseph', 'Bacho', 'AN149')
st12 = Student('Female', 25, 'Joana', 'Lucas', 'AN151')
print(st1)
print(st2)

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st11)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
try:
    gr.add_student(st11)
    gr.add_student(st12)
except MyException as err:
    print(f'{err.x}: {err.get_message()}\n')
print(gr)  # Only one student
gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

try:
    gr.add_student(st2)
    gr.add_student(st12)
except MyException as err:
    print(f'{err.x}: {err.get_message()}\n')

print(gr)