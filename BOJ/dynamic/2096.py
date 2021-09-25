# 210925 내려가기 gold4
import sys, copy

input = sys.stdin.readline

N = int(input())
res_list = [[0, 0, 0], [0, 0, 0]]
for _ in range(N):
    a, b, c = list(map(int, input().split()))
    temp = copy.deepcopy(res_list)
    res_list[0][0] = a + min(temp[0][0], temp[0][1])
    res_list[0][1] = b + min(temp[0][0], temp[0][1], temp[0][2])
    res_list[0][2] = c + min(temp[0][1], temp[0][2])
    res_list[1][0] = a + max(temp[1][0], temp[1][1])
    res_list[1][1] = b + max(temp[1][0], temp[1][1], temp[1][2])
    res_list[1][2] = c + max(temp[1][1], temp[1][2])

print(max(res_list[1]), min(res_list[0]))


