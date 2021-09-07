# 210907
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = list(map(int, input().split()))

    def dfs(current=0, remain=M, last=0):
        result = current
        for i in range(last, N):
            score, time = problem_list[i]
            if remain - time >= 0:
                result = max(result, dfs(current + score, remain - time, i + 1))
            result = max(result, dfs(current, remain, i + 1))
        return result

    problem_list = []
    for _ in range(N):
        problem_list.append(list(map(int, input().split())))

    return [[str(dfs())]]

if __name__ == "__main__":
    print(solution(examine=True))


