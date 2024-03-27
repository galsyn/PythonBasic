yes_ = 'yes'
while yes_.lower() == 'yes' or yes_.lower() == 'y':
    check_n = True
    while check_n:
        lst = []
        dots = False
        x = input('Enter first number: ')
    # check if x is a number
        for el in x:
            if el.isdigit():
                lst.append(True)
            elif el == '.' and not dots:
                lst.append(True)
                dots = True
            else:
                lst.append(False)
        if all(lst):
            check_n = False
        else:
            print('You input incorrect number!')
        if x == '' or x == '.':
            x = 0
            check_n = False
    x = float(x)
    check_n = True
    while check_n:
        lst = []
        dots = False
        y = input('Enter second number: ')
    # check if y is a number
        for el in y:
            print(el)
            if el.isdigit():
                lst.append(True)
            elif el == '.' and not dots:
                lst.append(True)
                dots = True
            else:
                lst.append(False)
        if all(lst):
            check_n = False
        else:
            print('You input incorrect number!')
        if y == '' or y == '.':
            y = 0
            check_n = False
    y = float(y)
    operator = input('Enter operation (+,-,*,/ or **): ')
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    elif operator == "*":
        print(x * y)
    elif operator == "**":
        print(x ** y)
    elif operator == "/":
        if y == 0:
            print('Error! Division by zero!')
        else:
            print(x / y)
    else:
        print('Unknown operator!')    # if user enters something else than '+,-,*,**,/'
    yes_ = input('Continue? (yes/no): ')
