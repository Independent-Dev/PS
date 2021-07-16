# 210711 용돈관리 silver3
import sys

def Count():
    result = 0
    temp = 0
    for a in arr:
        if mid < a:
            return M + 1
        if temp < a:
            temp = mid - a
            result += 1
        else:
            temp -= a

    return result

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

end = sum(arr)
start = 0  # 왜 초기값이 0이어야 하나... 왜 min(arr)로 하면 틀리게 되는 것인가...
result = end

while start <= end:
    mid = (start + end) // 2
    if Count() <= M:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
