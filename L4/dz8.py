# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0
el_sum = 0
lst = [0, 1, 7, 2, 4, 8]
if len(lst) > 0:
    for el in lst[::2]:
        el_sum += el
    el_sum *= lst[-1]
print(el_sum)

# Another way to get elements with even index
el_sum = 0
lst = [5]
if len(lst) > 0:
    for i in range(0, len(lst), 2):
        print(i, lst[i])
        el_sum += lst[i]
    el_sum *= lst[-1]
print(el_sum)
