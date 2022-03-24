# 210727
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(x=0, res=0):
        if x < N and res < C:
            return max(dfs(x + 1, res + arr[x]), dfs(x + 1, res))
        if res > C:
            return 0
        return res

    C, N = [int(x) for x in input().split()]
    arr = []

    for _ in range(N):
        arr.append(int(input()))

    MAX = sum(arr)

    return [str(dfs()) if MAX > C else str(MAX)]


if __name__ == "__main__":
    print(solution(examine=True))
