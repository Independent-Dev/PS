from sys import stdin
from collections import deque, defaultdict

t_num = int(input())
box_num = []
night_position = []
target = []
result = []

# 입력받기
for _ in range(t_num):
    box_num.append(int(input()))
    night_position.append(list(map(int, stdin.readline().strip().split())))
    target.append(list(map(int, stdin.readline().strip().split())))

# calculate
def bfs(box_num, np, target):
    graph = defaultdict(lambda : defaultdict(int))

    graph[np[0]][np[1]] = 1
    dq = deque([np])
    res = 0
    while True:
        for j in range(len(dq)):
            x, y = dq.popleft()
            if [x, y] == target:
                result.append(res)
                return
            for m, n in ([x + 2, y+1], [x+2, y-1], [x-2, y+1], [x-2, y-1],
                         [x+1, y+2], [x+1, y-2], [x-1, y+2], [x-1, y-2]):
                if 0<=m<box_num and 0<=n<box_num and graph[m][n] == 0:
                    graph[m][n] = 1
                    dq.append([m, n])
        res += 1


for i in range(t_num):
    bfs(box_num[i], night_position[i], target[i])

for res in result:
    print(res)
