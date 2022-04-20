from examine import examine
import sys, math

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
    factorial_N, base = math.factorial(N), 1
    target = [factorial_N] * N
    answer = []
    for i in range(1, N + 1):
        target[i - 1] /= factorial_N
        if i != N:
            factorial_N = factorial_N * i / (N - i)

    dfs()

    return [' '.join(answer)]


if __name__ == "__main__":
    print(solution(examine=True))
