# 210825
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(current_value = 0, count = 0):
        nonlocal temp_min
        if current_value == M:
            temp_min = min(count, temp_min)
            return count
        elif count > temp_min or current_value > M:
            return M
        return min(dfs(current_value + a, count + 1) for a in arr)
        

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    M = int(input())
    temp_min = M
    
    return [[str(dfs())]]

if __name__ == "__main__":
    print(solution(examine=True))
