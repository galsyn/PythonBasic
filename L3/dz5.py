# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]
old_lst = []
new_lst = []
if len(old_lst) % 2 == 0:
    middle_index = len(old_lst) // 2    # if even quantity of elements in old_lst
else:
    middle_index = len(old_lst) // 2 + 1    # if odd quantity  of elements in old_lst
left_lst = old_lst[:middle_index]    # if len(old_lst = 0, left_lst = []
right_lst = old_lst[middle_index:]    # if len(old_lst) = 1 or 0, right_lst = []
new_lst.append(left_lst)
new_lst.append(right_lst)
print(new_lst)
