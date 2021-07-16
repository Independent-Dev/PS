# 210716 공유기 설치 silver1
import sys

def Count():
    result = 1
    temp_mid = 0
    for g in arr_gap:
        temp_mid += g
        if temp_mid >= mid:
            temp_mid = 0
            result += 1

    return result

input = sys.stdin.readline
N, C = map(int, input().split())
arr = sorted([int(input().strip()) for _ in range(N)])
result = 0
if C == 2:
    print(arr[-1] - arr[0])
else:
    arr_gap = [arr[i] - arr[i - 1] for i in range(1, N)]
    start, end = min(arr_gap), arr[-1] - arr[0]
    while start <= end:
        mid = (start + end) // 2
        if Count() < C:
            end = mid - 1
        else:
            result = max(result, mid)
            start = mid + 1

    print(result)