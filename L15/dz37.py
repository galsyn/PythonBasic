class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            square_ = self.get_square() + other.get_square()
            new_width = self.get_width(square_)
            return Rectangle(new_width, square_ / new_width)
        return NotImplemented

    @staticmethod
    def get_width(square):
        for i in [2, 3, 5, 7, 11]:
            if square % i == 0:
                return square / i
        return 1

    def __mul__(self, n):
        square_ = self.get_square() * n
        new_width = self.get_width(square_)
        return Rectangle(new_width, square_ / new_width)

    def __str__(self):
        return f"Rectangle sizes: {self.width} x {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'
print(r3)

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print(r4)

print(Rectangle(3, 6) == Rectangle(2, 9))
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print('Ok')
