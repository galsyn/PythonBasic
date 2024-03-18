# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
lst = [12, 3, 4, 10, 8]
if len(lst) != 0:   # if lst is not empty
    el = lst.pop()    # remove last element from lst
    lst.insert(0, el)   # and insert el at 0-position
print(lst)
