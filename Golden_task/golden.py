lst = [[7, 0], [5, 8, 0], [9, 8, 2, 0], [1, 3, 5, 6, 0], [6, 2, 4, 4, 5, 0], [9, 5, 3, 5, 5, 7, 0], [7, 4, 6, 4, 7, 6, 8]]
print(len(lst))
new_game = "yes"
while new_game == "yes" or new_game == "ye" or new_game == "y":
    sum_ = 0
    j = 0
    i = 0
    while i < len(lst):
        coord_x = True
        coord_y = True
        x = i
        while coord_y:
            y = int(input(f'Input coordinate y - {j} or {j + 1}: '))
            print(y)
            if y == j or y == j + 1:
                coord_y = False
            else:
                print('Error y!')
        coord = (x, y)
        print(coord)
        print(lst[i])
        print(lst[x][y])
        i += 1
        j = y
        sum_ += lst[x][y]
    print(f'You collect gold of {sum_}')
    new_game = input('New game? (yes/no): ').lower()


