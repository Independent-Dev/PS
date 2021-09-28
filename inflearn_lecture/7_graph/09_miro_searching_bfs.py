# 210928
from examine.examine import examine
import sys

MOVE_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]
MIRO_SIZE = 7

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    result = 0
    visited = [[0] * MIRO_SIZE for _ in range(MIRO_SIZE)]
    miro = []
    
    for _ in range(MIRO_SIZE):
        miro.append(list(map(int, input().split())))
    
    next_list = [(0, 0)]
    visited[0][0] = 1

    while next_list:
        result += 1
        temp = list()
        for cur_y, cur_x in next_list:
            for move_y, move_x in MOVE_LIST:
                next_y = cur_y + move_y
                next_x = cur_x + move_x
                if MIRO_SIZE > next_y >= 0 and MIRO_SIZE > next_x >= 0:
                    if not miro[next_y][next_x] and not visited[next_y][next_x]:
                        temp.append((next_y, next_x))
                        visited[next_y][next_x] = 1
        if visited[MIRO_SIZE - 1][MIRO_SIZE - 1]:
            break
        next_list = temp[:]
    else:
        result = -1

    return [[str(result)]]

if __name__ == "__main__":
    print(solution(examine=True))
