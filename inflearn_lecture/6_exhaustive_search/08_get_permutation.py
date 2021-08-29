# 210825
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(count, part = []):
        if count > M:
            res.append(list(map(str, part)))
        else:
            part_set = set(part)
            # breakpoint()
            for i in range(1, N + 1):
                if i not in part_set:
                    dfs(count + 1, part + [i])
        

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = list(map(int, input().split()))
    print(N, M)
    res = []
    dfs(1)
    
    return res + [[str(len(res))]]

if __name__ == "__main__":
    print(solution(examine=True))
