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

    res = [[math.inf] * (N + 1)] + [[math.inf] + [0] * N for _ in range(N)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == 1 and j == 1:
                res[i][j] = target[0][0]
            else:
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + target[i - 1][j - 1]

    return [str(res[N][N])]

if __name__ == "__main__":
    print(solution(examine=True))
