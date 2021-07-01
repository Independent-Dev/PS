# 210701
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, C = map(int, input().split())
    barns = sorted([int(input()) for _ in range(N)])
    barn_gap = list(barns[i] - barns[i - 1] for i in range(1, N))
    start, stop = min(barns[i] - barns[i - 1] for i in range(1, N)), barns[-1] - barns[0]
    result = 0
    while start <= stop:  # 이 while문 안의 기본 구조를 잘 기억하는 것이 중요하겠다...!!
        mid = (start + stop) // 2
        if Count(mid, barn_gap) < C:
            stop = mid - 1
        else:
            start = mid + 1
            result = max(result, max_gap(mid, barn_gap))
    return [str(result)]

def Count(mid, barn_gap):
    result = 1
    temp = 0
    for gap in barn_gap:
        if temp + gap >= mid:
            result += 1
            temp = 0
        else:
            temp += gap
    return result

def max_gap(mid, barn_gap):
    temp_min = sum(barn_gap)
    temp = 0
    for gap in barn_gap:
        temp += gap
        if temp >= mid:
            temp_min = min(temp_min, temp)
            temp = 0
    return temp_min

if __name__ == "__main__":
    print(solution(examine=True))

