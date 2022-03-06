# 210702
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = [int(num) for num in input().split()]
    passanger_list = sorted([int(num) for num in input().split()])
    start, end, count = 0, N - 1, 0
    while start < end:
        if passanger_list[start] + passanger_list[end] <= M:
            start += 1
        end -= 1
        count += 1

    count += (start == end)

    return [str(count)]


if __name__ == "__main__":
    print(solution(examine=True))