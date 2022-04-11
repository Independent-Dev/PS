from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(x=0, res=0, arr=''):
        if x == N:
            nonlocal answer
            if res == F and not answer:
                answer = arr.split()
        else:
            for i in range(1, N + 1):
                if str(i) not in arr:
                    dfs(x + 1, res + target[x] * i, arr + " " + str(i))

    N, F = [int(x) for x in input().split()]
    target = [1] * N
    answer = []
    for i in range(N):
        for j in range(i - 1, 0, -1):
            target[j] = target[j] + target[j-1]

    dfs()

    return [' '.join(answer)]


if __name__ == "__main__":
    print(solution(examine=True))
