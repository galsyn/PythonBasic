class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'Human: {self.first_name} {self.last_name}\ngender: {self.gender}\nage: {self:age}'
