def find_unique_value(some_list):
    my_dict = {}
    for i in some_list:
        if my_dict.get(i):
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for key in my_dict:
        if my_dict[key] == 1:
            return key

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
