
# 210928
# 문제를 잘못 읽어서 푸는 데 시간이 좀 더 걸렸음. 
from examine.examine import examine
import sys

MOVE_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    def dfs(cur_y, cur_x):
        if cur_y == end[0] and cur_x == end[1]:
            nonlocal result
            result += 1

        for move_y, move_x in MOVE_LIST:
            next_y = cur_y + move_y
            next_x = cur_x + move_x
            
            if LIMIT > next_y >= 0 and LIMIT > next_x >= 0 and not visited[next_y][next_x]:
                if mountine_map[cur_y][cur_x] >= mountine_map[next_y][next_x]:
                    continue
                visited[next_y][next_x] = 1
                dfs(next_y, next_x)
                visited[next_y][next_x] = 0

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    LIMIT = int(input())
    visited = [[0] * LIMIT for _ in range(LIMIT)]
    mountine_map = []
    result = 0
    MAX = -sys.maxsize
    MIN = sys.maxsize
    
    for i in range(LIMIT):
        mountine_map.append(list(map(int, input().split())))
        if MIN > min(mountine_map[-1]):
            MIN = min(mountine_map[-1])
            start = [i, mountine_map[-1].index(MIN)]
        if MAX < max(mountine_map[-1]):
            MAX = max(mountine_map[-1])
            end = [i, mountine_map[-1].index(MAX)]
    
    visited[start[0]][start[1]] = 1

    dfs(start[0], start[1])
    
    return [[str(result) if result else str(-1)]]

if __name__ == "__main__":
    print(solution(examine=True))
