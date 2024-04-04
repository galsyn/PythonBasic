def add_one(some_list):
    some_int = int("".join([str(y) for y in some_list])) + 1
    new_list = list(str(some_int))
    for i, el in enumerate(new_list):
        new_list[i] = int(el)
    return new_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
