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
    start, stop = min(barn_gap), sum(barn_gap)
    result = 0
    while start <= stop:  # TODO 이 while문 안의 기본 구조를 잘 기억하는 것이 중요하겠다...!!
        mid = (start + stop) // 2
        horse_count, temp_result = calculate(mid, barn_gap)
        if horse_count < C:
            stop = mid - 1
        else:
            start = mid + 1
            result = max(result, temp_result)
    return [str(result)]


def calculate(mid, barn_gap):
    temp_result = sum(barn_gap)
    horse_count = 1
    horse_gap = 0
    for gap in barn_gap:
        horse_gap += gap
        if horse_gap >= mid:
            temp_result = min(temp_result, horse_gap)
            horse_count += 1
            horse_gap = 0

    return horse_count, temp_result


if __name__ == "__main__":
    print(solution(examine=True))

