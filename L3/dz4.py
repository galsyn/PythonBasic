x = float(input('Enter first number: '))
y = float(input('Enter second number: '))
print(type(x), type(y))
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
