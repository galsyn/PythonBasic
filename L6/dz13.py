import string
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA
user_string = input('Введіть через дефіс дві літери: ')
index_1 = string.ascii_letters.find(user_string[0])
index_2 = string.ascii_letters.find(user_string[-1])
# for i in range(index_1, index_2 + 1):
#     print(string.ascii_letters[i], sep="", end="")
print(string.ascii_letters[index_1:index_2 + 1])
