# 210906
from examine.examine import examine
import sys
from collections import defaultdict

@examine
def solution(**kwargs):
    def dfs(part = {1}, last=1):
        if last == N:
            nonlocal result
            result += 1
        else:
            for k in graph[last]:
                if k not in part:
                    dfs(part | {k}, k)

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(M):
        key, val = list(map(int, input().split()))
        graph[key].append(val)
    result = 0

    dfs()

    return [[str(result)]]

if __name__ == "__main__":
    print(solution(examine=True))


