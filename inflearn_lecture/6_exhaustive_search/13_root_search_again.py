from examine import examine
import sys
from collections import defaultdict

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(start=1):
        if start == N:
            nonlocal res
            res += 1
        else:
            for next in dd[start]:
                if not visited[next]:
                    visited[next] = 1
                    dfs(next)
                    visited[next] = 0


    N, M = [int(x) for x in input().split()]

    dd = defaultdict(list)
    visited = [0] * (N + 1)
    for _ in range(M):
        start, end = [int(x) for x in input().split()]
        dd[start].append(end)

    res = 0
    visited[1] = 1
    dfs()

    return [str(res)]


if __name__ == "__main__":
    print(solution(examine=True))
