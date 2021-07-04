# https://shoark7.github.io/programming/algorithm/3-LIS-algorithms#4 참조
import math

# 완전탐색
def lis(arr):
    if not arr:
        return 0

    ret = 1
    for i in range(len(arr)):
        nxt = []
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                nxt.append(arr[j])
        ret = max(ret, 1 + lis(nxt))
    return ret

# 동적계획법
def lis(arr):
    arr = [-math.inf] + arr
    N = len(arr)
    cache = [-1] * N

    def find(start):
        if cache[start] != -1:
            return cache[start]

        ret = 0
        for nxt in range(start+1, N):
            if arr[start] < arr[nxt]:
                ret = max(ret, find(nxt) + 1)

        cache[start] = ret
        return ret

    return find(0)

print(lis([1, 2, 3]))