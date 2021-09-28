
# 210928
# 문제를 잘못 읽어서 푸는 데 시간이 좀 더 걸렸음. 
from examine.examine import examine
import sys

MOVE_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]
MIRO_SIZE = 7

@examine
def solution(**kwargs):
    def dfs(cur_y=0, cur_x=0):
        if cur_x == MIRO_SIZE - 1 and cur_y == MIRO_SIZE - 1:
            nonlocal result
            result += 1

        for move_y, move_x in MOVE_LIST:
            next_y = cur_y + move_y
            next_x = cur_x + move_x
            if MIRO_SIZE > next_y >= 0 and MIRO_SIZE > next_x >= 0 and not miro[next_y][next_x] and not visited[next_y][next_x]:
                visited[next_y][next_x] = 1
                dfs(next_y, next_x)
                visited[next_y][next_x] = 0

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    visited = [[0] * MIRO_SIZE for _ in range(MIRO_SIZE)]
    miro = []
    result = 0
    
    for _ in range(MIRO_SIZE):
        miro.append(list(map(int, input().split())))
    
    visited[0][0] = 1

    dfs()
    
    return [[str(result) if result else str(-1)]]

if __name__ == "__main__":
    print(solution(examine=True))
