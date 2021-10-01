
# 211001
from examine.examine import examine
import sys

MOVE_LIST = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

@examine
def solution(**kwargs):
    def bfs(first_y=0, first_x=0):
        cur_list = [(first_y, first_x)]
        island_map[first_y][first_x] = 0
        while cur_list:
            temp = list()
            for cur_y, cur_x in cur_list:
                for move_y, move_x in MOVE_LIST:
                    next_y = cur_y + move_y
                    next_x = cur_x + move_x
                    if map_size > next_y >= 0 and map_size > next_x >= 0 and island_map[next_y][next_x]:
                        island_map[next_y][next_x] = 0
                        temp.append((next_y, next_x))
            cur_list = temp[:]


    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    island_map = list()
    result = 0

    map_size = int(input())
    
    for _ in range(map_size):
        island_map.append(list(map(int, input().split())))

    for i in range(map_size):
        for j in range(map_size):
            if island_map[i][j]:
                result += 1
                bfs(i, j)
        
    return [[str(result)]]

if __name__ == "__main__":
    print(solution(examine=True))