import random
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]
# lst=[6, 3, 7]
lst = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print(lst)
new_list = lst[:3:2]
new_list.append(lst[-2])
print(new_list)
