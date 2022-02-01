import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    arr = input().split()
    MAX, MAX_idx = 0, 0
    for i, e in enumerate(arr):
        temp = sum(int(x) for x in e)
        if MAX < temp:
            MAX = temp
            MAX_idx = i
    return [str(arr[MAX_idx])]

if __name__ == "__main__":
    print(solution(examine=True))