from examine import examine
import sys, math

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(idx=0, count=0, sum=0):
        if count == M:
            if sum % divide == 0:
                nonlocal res
                res += 1
        elif idx < N:
            dfs(idx + 1, count + 1, sum + target[idx])
            dfs(idx + 1, count, sum)


    N, M = [int(x) for x in input().split()]
    target = [int(x) for x in input().split()]
    divide = int(input())
    res = 0
    # dfs()

    # 풀이에 나와있는 것
    from itertools import combinations
    for arr in combinations(target, M):
        if sum(arr) % divide == 0:
            res += 1

    return [str(res)]


if __name__ == "__main__":
    print(solution(examine=True))
