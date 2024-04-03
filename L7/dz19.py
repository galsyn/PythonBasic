import random

def common_elements():
    lst3 = [i for i in range(0, random.randint(10, 1000), 3)]
    lst5 = [i for i in range(0, random.randint(10, 1000), 5)]
    return set(lst3).intersection(set(lst5))

print(common_elements())
# print(sorted(common_elements())) - повертає список