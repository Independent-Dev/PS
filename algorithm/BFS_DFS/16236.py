# 210621 gold4
# bfs
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
SIZE, eaten_fishes_count = 2, 0  # 가장 처음에 아기 상어의 크기는 2, eaten_fishes_count는 해당 크기에서 먹은 고기의
result, sec = 0, 1
success_list = []
fishes = [[] for _ in range(N)]  # fishes[y][x]
direction = [(0, -1), (-1, 0), (1, 0), (0, 1)]
visited = [[False] * N for _ in range(N)]

for n in range(N):
    fishes[n] = list(map(int, input().split()))
    if 9 in fishes[n]:
        x = fishes[n].index(9)
        position_list, position_list_temp = [(n, x)], []  # y, x 순
        fishes[n][x] = 0  # 상어가 있는 위치 0으로 만들기
        visited[n][x] = True  # 상어가 있는 위치 0으로 만들기

while True:
    while position_list:
        for before_y, before_x in position_list:
            for d_y, d_x in direction:
                after_x, after_y = before_x + d_x, before_y + d_y
                if 0 <= after_x < N and 0 <= after_y < N and not visited[after_y][after_x] and fishes[after_y][after_x] <= SIZE:
                    if 0 < fishes[after_y][after_x] < SIZE:
                        heappush(success_list, (after_y, after_x))

                    position_list_temp.append((after_y, after_x))
                    visited[after_y][after_x] = True

        if success_list:
            after_y, after_x = heappop(success_list)
            position_list = [(after_y, after_x)]  # 위치 변경하기
            position_list_temp, success_list = [], []
            fishes[after_y][after_x] = 0  # 옮기는 위치 0으로 만들기
            visited[after_y][after_x] = True
            result += sec  # 시간 더하기
            sec = 1  # 시간 초기화
            visited = [[False] * N for _ in range(N)]  # visited 초기화
            eaten_fishes_count += 1  # eaten_fishes_count 변경

            if eaten_fishes_count == SIZE:  # 만약 eaten_fishes_count == size
                SIZE += 1  # size += 1
                eaten_fishes_count = 0

        else:
            position_list, position_list_temp = position_list_temp[:], []
            sec += 1  # 시간 늘이기
    else:
        print(result)
        break