import sys, math
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def binary_search(start, end):
        res = start
        while start <= end:
            limit = (start + end) // 2
            count = 1
            temp = 0
            for gap in arr_gap:
                if temp + gap >= limit:
                    temp = 0
                    count += 1
                else:
                    temp += gap
            if count < C:
                end = limit - 1
            elif count >= C:
                start = limit + 1
                res = max(res, limit)
        return res

    N, C = [int(x) for x in input().split()]
    arr = sorted([int(input()) for _ in range(N)])
    arr_gap = [a - arr[i] for i, a in enumerate(arr[1:])]
    if C == 2:
        res = arr[-1] - arr[0]
    else:
        start, end = min(arr_gap), (arr[-1] - arr[0]) // (C - 1)
        res = binary_search(start, end)

    return [str(res)]

if __name__ == "__main__":
    print(solution(examine=True))