# 210825
from examine.examine import examine
import sys

count = 0

@examine
def solution(**kwargs):
    def dfs(idx, part = 0):
        global count
        count += 1
        print(count)
        if part > C:
            return 0
        if idx < N:
            return max(dfs(idx + 1, part + target_list[idx]), dfs(idx + 1, part))
        return part

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    C, N = list(map(int, input().split()))
    target_list = [0] * N
    for i in range(N):
        target_list[i] = int(input().strip())
    
    return [[str(dfs(0))]]

if __name__ == "__main__":
    print(solution(examine=False))
