from examine import examine
import sys
from itertools import combinations

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    
    _ , K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    res = set()
    for e in combinations(arr, 3):
        res.add(sum(e))

    return [[str(sorted(list(res), reverse=True)[K - 1])]]

if __name__ == "__main__":
    print(solution(examine=True))
