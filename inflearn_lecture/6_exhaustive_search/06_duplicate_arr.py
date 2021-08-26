# 210825
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(next, part = []):
        if next <= M:
            for i in range(1, N + 1):
                dfs(next+1, part + [str(i)])
        else:
            res.append(part)
        

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = list(map(int, input().split()))
    res = []
    dfs(1)
    res.append([str(len(res))])
    
    return res

if __name__ == "__main__":
    print(solution(examine=True))
