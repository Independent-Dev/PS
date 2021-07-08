# 210614 silver2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    if 0 <= x < len(field) and 0 <= y < len(field[-1]) and field[x][y] == 1:
        global k
        k -= 1
        field[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

result_list = []

for _ in range(int(input())):
    m, n, k = [int(x) for x in input().split()]
    field = [[0] * n for _ in range(m)]

    for _ in range(k):
        p_x, p_y = input().split()
        field[int(p_x)][int(p_y)] = 1

    result, break_flag = 0, False

    for x in range(m):
        for y in range(n):
            if dfs(x, y):
                result += 1
            if k <= 0:
                break_flag = True
                break
        if break_flag:
            break

    result_list.append(result)

for result in result_list:
    print(result)
