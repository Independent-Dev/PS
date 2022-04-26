from examine import examine
import sys
from collections import defaultdict

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(idx=0, count=0, time=0):
        if time <= M:
            if idx == N:
                nonlocal res
                res = max(res, count)
            else:
                dfs(idx + 1, count + arr[idx][0], time + arr[idx][1])
                dfs(idx + 1, count, time)

    N, M = [int(x) for x in input().split()]

    arr = []
    for _ in range(N):
        arr.append([int(x) for x in input().split()])

    res = 0
    dfs()

    return [str(res)]

if __name__ == "__main__":
    print(solution(examine=True))
