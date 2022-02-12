import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def binary_search(start, end):
        idx = (start + end) // 2
        if arr[idx] > M:
            return binary_search(start, idx - 1)
        elif arr[idx] < M:
            return binary_search(idx + 1, end)
        else:
            return idx

    N, M = [int(x) for x in input().split()]
    arr = sorted([int(x) for x in input().split()])

    return [str(binary_search(0, N - 1) + 1)]

if __name__ == "__main__":
    print(solution(examine=True))