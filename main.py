from studentlib import *

print('Hello Student!')

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)   # Only one student

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
st13 = Student('Female', 25, 'Rina', 'Lucas', 'AN152')
print(st1)
print(st2)

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print(f"Total {len(gr.group)} students")

assert gr.find_student('Jobs') == st1, 'Test0'
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
print('OK')
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
    gr.add_student(st13)
except MyException as err:
    print(f'{err.x}: {err.get_message()}\n')
print(gr)  # Only one student
gr.delete_student('Taylor')
print(gr)
print(f"Total {len(gr.group)} students")

gr.delete_student('Taylor')  # No error!

try:
    gr.add_student(st12)
except MyException as err:
    print(f'{err.x}: {err.get_message()}\n')

print(gr)
print(f"Total {len(gr.group)} students")
