import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def binary_search(start, end):
        if start == end:
            return start
        idx = (start + end) // 2
        count = sum(a // idx for a in arr)
        if count < N:
            return binary_search(start, idx - 1)
        elif count >= N:
            return binary_search(idx + 1, end)

    K, N = [int(x) for x in input().split()]
    arr = sorted([int(input()) for _ in range(K)])

    return [str(binary_search(0, arr[-1]))]

if __name__ == "__main__":
    print(solution(examine=True))