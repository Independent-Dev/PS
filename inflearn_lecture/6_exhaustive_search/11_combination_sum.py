# 210903
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(part = set(), cur = 0):
        if len(part) >= K:
            if sum(part) % M == 0:
                nonlocal result
                result += 1

        else:
            for i in range(cur, N):
                if int_list[i] not in part:
                    dfs(part | {int_list[i]}, i + 1)

    # def dfs():
    #     for x in combinations(int_list, K):
    #         if sum(x) % M == 0:
    #             nonlocal result
    #             result += 1
        

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, K = list(map(int, input().split()))
    int_list = list(map(int, input().split()))
    M = int(input())
    result = 0
    dfs()

    return [[str(result)]]

if __name__ == "__main__":
    print(solution(examine=True))


