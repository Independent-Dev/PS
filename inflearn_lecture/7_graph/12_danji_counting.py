
# 211001
from examine.examine import examine
import sys

MOVE_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    def dfs(cur_y=0, cur_x=0):
        danji_map[cur_y][cur_x] = 0
        result_list[-1] += 1
        for move_y, move_x in MOVE_LIST:
            next_y = cur_y + move_y
            next_x = cur_x + move_x
            if danji_size > next_y >= 0 and danji_size > next_x >= 0 and danji_map[next_y][next_x]:
                dfs(next_y, next_x)

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    danji_map = list()
    result_list = []

    danji_size = int(input())
    
    for _ in range(danji_size):
        danji_map.append(list(map(int, input())))

    for i in range(danji_size):
        for j in range(danji_size):
            if danji_map[i][j]:
                result_list.append(0)
                dfs(i, j)
        
    return [[str(len(result_list))]] + [[str(result)] for result in sorted(result_list)]

if __name__ == "__main__":
    print(solution(examine=True))
