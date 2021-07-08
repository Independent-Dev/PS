# 210702
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())), reverse=True)
    start, end, count = 0, len(weights) - 1, 0
    while start <= end:
        count += 1
        if M - weights[start] >= weights[end]:
            end -= 1
        start += 1

    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=True))