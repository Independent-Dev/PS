# 210702
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    arr = [int(num) for num in input().split()]

    res = ''
    before = 0

    while before < arr[0] or before < arr[-1]:
        if before < arr[0] < arr[-1] or arr[-1] < before < arr[0]:
            res += 'L'
            before = arr.pop(0)
        else:
            res += 'R'
            before = arr.pop(-1)

    return [str(len(res)), res]


if __name__ == "__main__":
    print(solution(examine=True))