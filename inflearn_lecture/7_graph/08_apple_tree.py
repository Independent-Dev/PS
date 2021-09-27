# 210927
from examine.examine import examine
import sys

MOVE_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    result = 0
    N = int(input())
    MIDDLE = N//2
    visited = [[0] * N for _ in range(N)]
    graph = []
    
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    next_list = [[MIDDLE, MIDDLE]]
    visited[MIDDLE][MIDDLE] = 1
    result = graph[MIDDLE][MIDDLE]
    for _ in range(N // 2):
        temp = []
        for y, x in next_list:
            for y_move, x_move in MOVE_LIST:
                next_y = y + y_move
                next_x = x + x_move
                if not visited[next_y][next_x]:
                    temp.append((next_y, next_x))
                    visited[next_y][next_x] = 1
                    result += graph[next_y][next_x]
        next_list = temp[:]

    return [[str(result)]]

if __name__ == "__main__":
    print(solution(examine=True))
