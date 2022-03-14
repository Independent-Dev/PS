from examine.examine import examine
import sys
from collections import deque

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, K = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr = arr[K + 1:] + arr[:K + 1]
    count = 0
    same_count = 0
    MAX = 100
    for i, a in enumerate(arr):
        if a > arr[-1]:
            count += 1
            if a <= MAX:
                MAX = a
                same_count = 0

        elif a == arr[-1]:
            same_count += 1

    return [str(count + same_count)]

if __name__ == "__main__":
    print(solution(examine=True))