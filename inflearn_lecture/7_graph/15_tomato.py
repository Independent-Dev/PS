from examine import examine
import sys, pprint

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    direction = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    M, N = [int(num) for num in input().split()]

    next_red_tomato = []
    tomato_field = []

    day_count = 0
    green_tomato_count = 0

    for i in range(N):
        tomato_field.append([int(num) for num in input().split()])
        for j in range(M):
            if tomato_field[-1][j] == 1:
                next_red_tomato.append([i, j])
            elif tomato_field[-1][j] == 0:
                green_tomato_count += 1

    while True:
        temp_list = []
        for tomato_y, tomato_x in next_red_tomato:
            for dir_y, dir_x in direction:
                next_y, next_x = tomato_y + dir_y, tomato_x + dir_x
                if 0 <= next_y < N and 0 <= next_x < M and not tomato_field[next_y][next_x]:
                    temp_list.append([next_y, next_x])
                    tomato_field[next_y][next_x] = 1
                    green_tomato_count -= 1
        if temp_list:
            next_red_tomato = temp_list
            day_count += 1
        else:
            break

    return [str(day_count if not green_tomato_count else -1)]

if __name__ == "__main__":
    print(solution(examine=True))
