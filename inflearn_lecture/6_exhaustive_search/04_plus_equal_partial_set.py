# 210825
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(idx, part = 0):
        if part == half_sum:
            return True
        if idx < N:
            return dfs(idx + 1, part + target_list[idx]) or dfs(idx + 1, part)

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    target_list = list(map(int, input().strip().split()))
    half_sum = sum(target_list) / 2
    
    return [['YES' if dfs(0) else 'NO']]

if __name__ == "__main__":
    print(solution(examine=True))
