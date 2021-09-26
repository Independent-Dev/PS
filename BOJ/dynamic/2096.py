# 210925 내려가기 gold4
# 210926 다시 풀음
import sys, copy

input = sys.stdin.readline
function_list = [max, min]

N = int(input())
res_list = [[0, 0, 0], [0, 0, 0]]
for _ in range(N):
    a, b, c = list(map(int, input().split()))
    temp = copy.deepcopy(res_list)
    for i, function in enumerate(function_list):
        res_list[i][0] = a + function(temp[i][0], temp[i][1])
        res_list[i][1] = b + function(temp[i][0], temp[i][1], temp[i][2])
        res_list[i][2] = c + function(temp[i][1], temp[i][2])

print(max(res_list[0]), min(res_list[1]))


