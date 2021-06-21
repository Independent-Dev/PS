# 210621 N과 M(5) silver3
# backtracking

def solve(length):
    if length == M:
        print(' '.join(list(map(str, arr))))
        return

    for i, t in enumerate(target):
        if not visited[i]:
            arr[length] = t
            visited[i] = True
            solve(length + 1)
            visited[i] = False

N, M = list(map(int, input().split()))
target = sorted(list(map(int, input().split())))
visited = [False] * len(target)
arr = [0] * M
solve(0)
