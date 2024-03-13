x = int(input('Enter a 5-digit integer: '))  # if x = 12345
x1, y = divmod(x, 10000)  # x1 = 1, y = 2345
x2, y = divmod(y, 1000)   # x2 = 2, y = 345
x3, y = divmod(y, 100)   # x3 = 3, y = 45
x4, y = divmod(y, 10)    # x4 = 4, y = 5
x = y * 10000 + x4 * 1000 + x3 * 100 + x2 * 10 + x1
print(x)
