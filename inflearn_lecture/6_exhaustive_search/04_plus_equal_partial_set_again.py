# 210727
from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(x=0, res=0):
        if res == target:
            nonlocal ret
            ret = 'YES'
        elif x < N and res < target:
            dfs(x + 1, res + arr[x])
            dfs(x + 1, res)

    N = int(input())
    arr = [int(s) for s in input().split()]
    target = sum(arr) / 2
    ret = 'NO'
    dfs()

    return [ret]


if __name__ == "__main__":
    print(solution(examine=True))
