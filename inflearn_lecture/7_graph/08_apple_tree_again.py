from examine import examine
import sys

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    center = N // 2
    field = []
    for _ in range(N):
        field.append([int(num) for num in input().split()])

    pos_list = [(center, center)]
    count = field[center][center]
    field[center][center] = 0

    for _ in range(center):
        temp_pos = []
        for cur_y, cur_x in pos_list:
            for offset_y, offset_x in OFFSET_LIST:
                next_x, next_y = cur_x + offset_x, cur_y + offset_y
                if field[next_y][next_x]:
                    count += field[next_y][next_x]
                    field[next_y][next_x] = 0
                    temp_pos.append((next_y, next_x))
        pos_list = temp_pos

    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=True))
