# 210621 N과 M(4) silver3
# backtracking
def solve(length):
    if length == M:
        print(' '.join(list(map(str, arr[1:]))))
        return

    for n in range(1, N + 1):
        if arr[length] <= n:
            arr[length + 1] = n
            solve(length + 1)

N, M = list(map(int, input().split()))
arr = [0] * (M + 1)
solve(0)
