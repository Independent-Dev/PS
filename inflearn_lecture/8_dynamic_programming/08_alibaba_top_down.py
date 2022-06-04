from examine import examine
import sys, math

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    target = []
    for i in range(N):
        target.append([int(num) for num in input().split()])

    res = [[0] * N for _ in range(N)]
    res[0][0] = target[0][0]

    def dfs(y=N-1, x=N-1):
        if y < 0 or x < 0:
            return math.inf

        if not res[y][x]:
            res[y][x] = target[y][x] + min(dfs(y-1, x), dfs(y, x-1))

        return res[y][x]

    return [str(dfs())]

if __name__ == "__main__":
    print(solution(examine=True))
