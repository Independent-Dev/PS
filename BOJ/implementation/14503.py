# 210612
# not solved
import sys

def is_in_map(x, y):
    return 0 < x < M-1 and 0 < y < N-1

def robot():
    direction = ((0, -1), (1, 0), (0, 1), (-1, 0))  # north east south west
    x, y, current_dir = [int(number) for number in sys.stdin.readline().split()]
    count, dir_count = 0, 0

    for _ in range(N):
        map.append([int(number) for number in sys.stdin.readline().split()])

    while True:
        if map[y][x] == 0:
            map[y][x] = 1
            count += 1
        current_dir = (current_dir + 3) % 4
        while not is_in_map(x + direction[current_dir % 4][0], y + direction[current_dir % 4][1]) or map[y + direction[current_dir % 4][1]][x + direction[current_dir % 4][0]]:
            dir_count += 1
            if dir_count == 4:
                x -= direction[(current_dir) % 4][0]
                y -= direction[(current_dir) % 4][1]
                if not is_in_map(x, y):
                    return count
                else:
                    break
            current_dir = (current_dir + 3) % 4

        else:
            x += direction[current_dir % 4][0]
            y += direction[current_dir % 4][1]
        dir_count = 0

N, M = [int(x) for x in sys.stdin.readline().split()]  # N이 세로, M이 가로
map = []
print(robot())
for m in map:
    print(m)


