import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    arr = list(str(x) for x in range(1, 21))
    for _ in range(10):
        start, end = [int(x) for x in input().split()]
        arr[start - 1:end] = arr[end-1::-1] if start == 1 else arr[end-1:start-2:-1]

    return [' '.join(arr)]

if __name__ == "__main__":
    print(solution(examine=True))