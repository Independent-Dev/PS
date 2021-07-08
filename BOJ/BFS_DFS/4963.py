# 210614
import sys
input = sys.stdin.readline
def dfs(x, y, w, h, i):
    if 0<= x < w and 0 <= y < h and globe[i][y][x] == 1:
        globe[i][y][x] = 0
        for dir_x, dir_y in direction:
            dfs(x + dir_x, y + dir_y, w, h, i)
        return True

globe = []
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
size = [list(map(int, input().split()))]
result = 0

while not(size[-1][0] == size[-1][1] == 0):
    globe.append(list())
    for _ in range(size[-1][1]):
        globe[-1].append(list(map(int, input().split())))

    size.append(list(map(int, input().split())))

for i, (w, h) in enumerate(size[:-1]):
    for y in range(h):
        for x in range(w):
            if dfs(x, y, w, h, i):
                result += 1
    print(result)
    result = 0
