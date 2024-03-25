import keyword
import string

keyword_list = keyword.kwlist
res = True
my_string = input('Input your string: ')
# check if my_string begins with number (and consist of numbers only)
for num in list(range(0, 9)):
    if my_string[0] == str(num):
        res = False
        break
# check if my_string coincides with keyword
for el in keyword_list:
    if my_string == el:
        res = False
        break
# check if my_string has big letters
if my_string.lower() != my_string:
    res = False
# check if my_string has spaces
for el in my_string:
    if el == ' ':
        res = False
        break
# check if my_string has punctuation symbols
for i in string.punctuation:
    for el in my_string:
        if el == i and el !='_':
            res = False
            break
if my_string[0] == '_' and len(my_string) > 1:
    r = 0
    for i in range(len(my_string)):
        if my_string[i] == '_':
            r +=1
    if r ==  len(my_string):
        res = False
print('Is the name correct? ', res)
