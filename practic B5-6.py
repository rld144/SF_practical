def greet():
    print(' '*7, " Начинаем игру")
    print(' '*7, "КРЕСТИКИ-НОЛИКИ")
    print(' '*7, '_'*15)

def check(grid):
    for i in range(1, 4):
        if all([grid[i][1] == grid[i][2] == grid[i][3], grid[i][1] != '-']) or \
                all([grid[1][i] == grid[2][i] == grid[3][i], grid[1][i] != '-']):
            return True
    if all([grid[1][1] == grid[2][2] == grid[3][3], grid[1][1] != '-']) or \
            all([grid[1][3] == grid[2][2] == grid[3][1], grid[1][3] != '-']):
        return True
    return False

def input_(grid, prev_mark):
    while True:
        while True:
            i = input("введи координаты по № строки: ")
            if i in ['1', '2', '3']:
                break
            else:
                print("!вы ввели не то!")
        while True:
            j = input("введи координаты по № столбца: ")
            if j in ['1', '2', '3']:
                break
            else:
                print("!вы ввели не то!")
        if grid[int(i)][int(j)] == '-':
            break
        else:
            print('!ячейка занята!')

    while True:
        mark = input("введи крест или ноль (x или 0): ")
        if mark in ['x', '0']:
            if mark != prev_mark:
                break
            else:
                print("!вы перепутали, введите другой символ!")
        else:
            print("!вы ввели не тот знак!")
    return i, j, mark

greet()
grid = [['-' for i in range(4)] for x in range(4)]
for i in range(4):
    grid[0][i] = i
    grid[i][0] = i
grid[0][0] = ' '
for i in grid:
    print(' ' * 10, *i)

num_step = 0
prev_mark = None
while True:
    y, x, mark = input_(grid, prev_mark)
    grid[int(y)][int(x)] = mark
    prev_mark = mark

    print('_' * 30)
    for i in grid:
        print(' '*10, *i)
    print('_' * 30)

    if check(grid):
        print(mark, "you WINNER")
        break

    num_step += 1

    if num_step == 9:
        print('НИЧЬЯ!!!')
        break
