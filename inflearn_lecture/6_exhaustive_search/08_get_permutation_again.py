# 220328
from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(x = 0, arr = []):
        if x == M:
            res.append(' '.join(arr))
        else:
            for i in range(1, N + 1):
                if not visited[i]:
                    visited[i] = True
                    dfs(x + 1, arr + [str(i)])
                    visited[i] = False

    N, M = [int(x) for x in input().split()]
    res, visited = [], [False] * (N + 1)
    dfs()

    return res + [str(len(res))]


if __name__ == "__main__":
    print(solution(examine=True))
