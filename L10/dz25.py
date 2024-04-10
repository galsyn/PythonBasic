from inspect import isgenerator


def pow_(x):
    return x ** 2


def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    i = 0
    while i < end:
        yield begin
        begin = func(begin)
        i += 1


gen = some_gen(2, 4, pow_)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
