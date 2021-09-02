# 210901
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(count, part = [], sum = 0):
        if count > N:
            if sum == M:
                return [str(p) for p in part]
            return 0
            
        else:
            part_set = set(part)
            # breakpoint()
            for i in range(1, N + 1):
                if i not in part_set:
                    flag = dfs(count + 1, part + [i], sum + (binomial[count - 1] * i))
                    if flag:
                        return flag
        

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = list(map(int, input().split()))
    binomial = [1] * N
    for i in range(1, N):
        binomial[i] = binomial[i - 1] * (N - i) // i
    
    return [dfs(1)]

if __name__ == "__main__":
    print(solution(examine=True))