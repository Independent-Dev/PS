# 210611
import sys
input = sys.stdin.readline

def AC():
    commands = input().strip()
    _ = input()
    array = eval(input().strip())
    index = [0, 0, len(array)]
    step = 1
    for command in commands:
        if command == 'R':
            step *= -1
        else:
            index[step] += step
        if index[1] > index[-1]:
            return 'error'

    return str(array[index[1]:index[-1]][::step])

for _ in range(int(input())):
    print(AC().replace(" ", ''))