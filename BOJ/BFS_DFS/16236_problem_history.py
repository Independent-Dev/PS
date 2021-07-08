# 210620 gold4 for prac
# bfs

# v1 -------------------------
import sys
input = sys.stdin.readline

N = int(input())
SIZE = 2  # 가장 처음에 아기 상어의 크기는 2
eaten_fishes_count = 0  #
result, sec = 0, 1
fishes = [[] for _ in range(N)]  # fishes[y][x]
direction = [(0, -1), (-1, 0), (1, 0), (0, 1)]
visited = [[False] * N for _ in range(N)]

def can_visit(x, y):
    return 0 <= x < N and 0 <= y < N and not visited[y][x]

for n in range(N):
    fishes[n] = list(map(int, input().split()))
    if 9 in fishes[n]:
        position_list, position_list_temp = [(fishes[n].index(9), n)], []
        visited[n][fishes[n].index(9)] = True
        fishes[n][fishes[n].index(9)] = 0  # 상어가 있는 위치 0으로 만들기

for f in fishes:
    print(f)

print("SIZE: {}".format(SIZE))

while True:
    while position_list:
        try:
            # print(f"position_list: {position_list}, position_list_temp: {position_list_temp}")
            for f_x, f_y in position_list:
                for d_x, d_y in direction:
                    after_x, after_y = f_x + d_x, f_y + d_y
                    # print(f"after_x: {after_x}, after_y: {after_y}")
                    if can_visit(after_x, after_y) and fishes[after_y][after_x] <= SIZE:
                        if 0 < fishes[after_y][after_x] < SIZE:
                            position_list = [(after_x, after_y)]  # 위치 변경하기
                            position_list_temp = []
                            fishes[after_y][after_x] = 0  # 옮기는 위치 0으로 만들기
                            print(f"result: {result}, sec: {sec}")
                            for f in fishes:
                                print(f)
                            result += sec  # 시간 더하기
                            sec = 1  # 시간 초기화
                            visited = [[False] * N for _ in range(N)]  # visited 초기화
                            visited[after_y][after_x] = True
                            eaten_fishes_count += 1  # eaten_fishes_count 변경

                            print(f"eaten_fishes_count: {eaten_fishes_count}, x: {after_x}, y: {after_y} ")
                            if eaten_fishes_count == SIZE:  # 만약 eaten_fishes_count == size
                                SIZE += 1  # size += 1
                                print("SIZE: {}".format(SIZE))
                                eaten_fishes_count = 0

                            raise NotImplementedError  # break
                        else:
                            position_list_temp.append((after_x, after_y))
                            visited[after_y][after_x] = True

            position_list, position_list_temp = position_list_temp[:], []
            # for v in visited:
            #     print(v)
            # print(f"sec: {sec}")
            sec += 1  # 시간 늘이기
        except Exception as e:
            print(e)
            break
    else:
        print("---------------------")
        print(result)
        break

# ----------------------------------
# ----------------------------------
# v2 -------------------------------
# 210620 gold4
# bfs
import sys
input = sys.stdin.readline

N = int(input())
SIZE = 2  # 가장 처음에 아기 상어의 크기는 2
eaten_fishes_count = 0  #
result, sec = 0, 1
fishes = [[] for _ in range(N)]  # fishes[y][x]
direction = [(0, -1), (-1, 0), (1, 0), (0, 1)]
visited = [[False] * N for _ in range(N)]

def can_visit(x, y):
    return 0 <= x < N and 0 <= y < N and not visited[y][x]

for n in range(N):
    fishes[n] = list(map(int, input().split()))
    if 9 in fishes[n]:
        position_list, position_list_temp = [(n, fishes[n].index(9) )], []  # y, x 순
        visited[n][fishes[n].index(9)] = True
        fishes[n][fishes[n].index(9)] = 0  # 상어가 있는 위치 0으로 만들기

for f in fishes:
    print(f)

print("SIZE: {}".format(SIZE))

while True:
    while position_list:
        try:
            # print(f"position_list: {position_list}, position_list_temp: {position_list_temp}")
            for f_y, f_x in position_list:
                for d_x, d_y in direction:
                    after_x, after_y = f_x + d_x, f_y + d_y
                    # print(f"after_x: {after_x}, after_y: {after_y}")
                    if can_visit(after_x, after_y):
                        if 0 < fishes[after_y][after_x] < SIZE:
                            position_list = [(after_y, after_x)]  # 위치 변경하기
                            position_list_temp = []
                            fishes[after_y][after_x] = 0  # 옮기는 위치 0으로 만들기
                            print(f"result: {result}, sec: {sec}")
                            for f in fishes:
                                print(f)
                            result += sec  # 시간 더하기
                            sec = 1  # 시간 초기화
                            visited = [[False] * N for _ in range(N)]  # visited 초기화
                            visited[after_y][after_x] = True
                            eaten_fishes_count += 1  # eaten_fishes_count 변경

                            print(f"eaten_fishes_count: {eaten_fishes_count}, x: {after_x}, y: {after_y} ")
                            if eaten_fishes_count == SIZE:  # 만약 eaten_fishes_count == size
                                SIZE += 1  # size += 1
                                print("SIZE: {}".format(SIZE))
                                eaten_fishes_count = 0

                            raise NotImplementedError  # break
                        else:
                            position_list_temp.append((after_y, after_x))
                            visited[after_y][after_x] = True

            position_list, position_list_temp = sorted(position_list_temp[:]), []
            # for v in visited:
            #     print(v)
            # print(f"sec: {sec}")
            sec += 1  # 시간 늘이기
        except Exception as e:
            print(e)
            break
    else:
        print("---------------------")
        print(result)
        break

# ----------------------------------
# ----------------------------------
# v2 -------------------------------
# 210620 gold4
# bfs
import sys
input = sys.stdin.readline

N = int(input())
SIZE = 2  # 가장 처음에 아기 상어의 크기는 2
eaten_fishes_count = 0  #
result, sec = 0, 1
fishes = [[] for _ in range(N)]  # fishes[y][x]
direction = [(0, -1), (-1, 0), (1, 0), (0, 1)]
visited = [[False] * N for _ in range(N)]
FIND = False

def can_visit(x, y):
    return 0 <= x < N and 0 <= y < N and not visited[y][x]

for n in range(N):
    fishes[n] = list(map(int, input().split()))
    if 9 in fishes[n]:
        position_list, position_list_temp = [(n, fishes[n].index(9) )], []  # y, x 순
        visited[n][fishes[n].index(9)] = True
        fishes[n][fishes[n].index(9)] = 0  # 상어가 있는 위치 0으로 만들기

# for f in fishes:
#     print(f)
#
# print("SIZE: {}".format(SIZE))

while True:
    while position_list:
        # try:
        # print(f"position_list: {position_list}, position_list_temp: {position_list_temp}")
        success_list = []
        for f_y, f_x in position_list:
            for d_x, d_y in direction:
                after_x, after_y = f_x + d_x, f_y + d_y
                # print(f"after_x: {after_x}, after_y: {after_y}")
                if can_visit(after_x, after_y):
                    if 0 < fishes[after_y][after_x] < SIZE:
                        FIND = True
                        success_list.append((after_y, after_x))

                    # else:
                    position_list_temp.append((after_y, after_x))
                    visited[after_y][after_x] = True
        if FIND:
            print(success_list)
            after_y, after_x = sorted(success_list)[0]
            position_list = [(after_y, after_x)]  # 위치 변경하기
            position_list_temp = []
            fishes[after_y][after_x] = 0  # 옮기는 위치 0으로 만들기
            # print(f"result: {result}, sec: {sec}")
            # for f in fishes:
            #     print(f)
            result += sec  # 시간 더하기
            sec = 1  # 시간 초기화
            visited = [[False] * N for _ in range(N)]  # visited 초기화
            visited[after_y][after_x] = True
            eaten_fishes_count += 1  # eaten_fishes_count 변경
            FIND = False

            print(f"eaten_fishes_count: {eaten_fishes_count}, x: {after_x}, y: {after_y} ")
            if eaten_fishes_count == SIZE:  # 만약 eaten_fishes_count == size
                SIZE += 1  # size += 1
                print("SIZE: {}".format(SIZE))
                eaten_fishes_count = 0

        else:
            position_list, position_list_temp = sorted(position_list_temp[:]), []
            # for v in visited:
            #     print(v)
            # print(f"sec: {sec}")
            sec += 1  # 시간 늘이기
        # except Exception as e:
        #     print(e)
        #     break
    else:
        print("---------------------")
        print(result)
        break

# -----------------------------------
# -----------------------------------
# 210620 gold4
# bfs
import sys
input = sys.stdin.readline

N = int(input())
SIZE = 2  # 가장 처음에 아기 상어의 크기는 2
eaten_fishes_count = 0  #
result, sec = 0, 1
fishes = [[] for _ in range(N)]  # fishes[y][x]
direction = [(0, -1), (-1, 0), (1, 0), (0, 1)]
visited = [[False] * N for _ in range(N)]
FIND = False

def can_visit(x, y):
    return 0 <= x < N and 0 <= y < N and not visited[y][x]

for n in range(N):
    fishes[n] = list(map(int, input().split()))
    if 9 in fishes[n]:
        position_list, position_list_temp = [(n, fishes[n].index(9) )], []  # y, x 순
        visited[n][fishes[n].index(9)] = True
        fishes[n][fishes[n].index(9)] = 0  # 상어가 있는 위치 0으로 만들기

# for f in fishes:
#     print(f)
#
# print("SIZE: {}".format(SIZE))

while True:
    while position_list:
        # try:
        # print(f"position_list: {position_list}, position_list_temp: {position_list_temp}")
        success_list = []
        for f_y, f_x in position_list:
            for d_x, d_y in direction:
                after_x, after_y = f_x + d_x, f_y + d_y
                # print(f"after_x: {after_x}, after_y: {after_y}")
                if can_visit(after_x, after_y) and fishes[after_y][after_x] <= SIZE:
                    if 0 < fishes[after_y][after_x] < SIZE:
                        FIND = True
                        success_list.append((after_y, after_x))

                    # else:
                    position_list_temp.append((after_y, after_x))
                    visited[after_y][after_x] = True
        if FIND:
            print(success_list)
            after_y, after_x = sorted(success_list)[0]
            position_list = [(after_y, after_x)]  # 위치 변경하기
            position_list_temp = []
            fishes[after_y][after_x] = 0  # 옮기는 위치 0으로 만들기
            # print(f"result: {result}, sec: {sec}")
            for f in fishes:
                print(f)
            result += sec  # 시간 더하기
            sec = 1  # 시간 초기화
            visited = [[False] * N for _ in range(N)]  # visited 초기화
            visited[after_y][after_x] = True
            eaten_fishes_count += 1  # eaten_fishes_count 변경
            FIND = False

            print(f"eaten_fishes_count: {eaten_fishes_count}, x: {after_x}, y: {after_y} ")
            if eaten_fishes_count == SIZE:  # 만약 eaten_fishes_count == size
                SIZE += 1  # size += 1
                print("SIZE: {}".format(SIZE))
                eaten_fishes_count = 0

        else:
            position_list, position_list_temp = sorted(position_list_temp[:]), []
            # for v in visited:
            #     print(v)
            # print(f"sec: {sec}")
            sec += 1  # 시간 늘이기
        # except Exception as e:
        #     print(e)
        #     break
    else:
        print("---------------------")
        print(result)
        break

# 문제 분석
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
