# 210825
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def check(part):
        res = part[::]
        i = len(part)
        for k in range(i-1, 0, -1):
            for j in range(k):
                res[j] += res[j + 1]

        if res[0] == M:
            return [str(p) for p in part]
        else:
            return []

    def dfs(count, part = []):
        if count > N:
            return check(part)
            
        else:
            part_set = set(part)
            # breakpoint()
            for i in range(1, M + 1):
                if i not in part_set:
                    flag = dfs(count + 1, part + [i])
                    if flag:
                        return flag
        

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = list(map(int, input().split()))
    dfs(1)
    
    return [dfs(1)]

if __name__ == "__main__":
    print(solution(examine=False))