from inspect import isgenerator

def simple_number(num):
    for j in range(2, num // 2 + 1):
        if num != j and num % j == 0:
            return False
    return True

def prime_generator(end):
    i = 2
    while i <= end:
        if simple_number(i):
            yield i
        i += 1

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
