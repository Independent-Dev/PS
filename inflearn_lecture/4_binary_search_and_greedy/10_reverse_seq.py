# 210702
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    arr = [int(num) for num in input().split()]

    res = [N] * N
    for i, a in enumerate(arr, start=1):
        idx = 0
        # if a > 0:
        #     while a > 0 or res[idx] < i:
        #         if res[idx] > i:
        #             a -= 1
        #         idx += 1
        # else:
        #     while res[idx] < i:
        #         idx += 1

        while a > 0:
            if res[idx] > i:
                a -= 1
            idx += 1

        while res[idx] < i:
            idx += 1

        res[idx] = i

    return [' '.join(str(r) for r in res)]


if __name__ == "__main__":
    print(solution(examine=True))