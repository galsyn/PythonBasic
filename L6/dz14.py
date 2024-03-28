# 1000 -> 0, 423 -> 8, 33 -> 9 ,  25 -> 0, 1 -> 1
user_number = input('Input integer number: ')
if not user_number.isdigit():
    print('You don\'t input an integer number!')
else:
    if int(user_number) <= 9:
        print(user_number)
    else:
        while int(user_number) > 9:
            res = int(user_number[0])
            for i in user_number[1:]:
                res *= int(i)
            user_number = str(res)
        print(user_number)
