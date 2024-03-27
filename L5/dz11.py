import string

yes_ = 'yes'
while yes_.lower() == 'yes' or yes_.lower() == 'y':
    x = float(input('Enter first number: '))
    y = float(input('Enter second number: '))
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
        print('Unknown operator!')  # if user enters something else than '+,-,*,**,/'

    yes_ = input('Continue? (yes/no): ')

