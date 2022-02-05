import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    arr = [int(inp) for inp in input().split()]
    total_score = 0
    prev_score = 0
    for a in arr:
        if a:
            prev_score += 1
            total_score += prev_score
        else:
            prev_score = 0

    return [str(total_score)]

if __name__ == "__main__":
    print(solution(examine=True))