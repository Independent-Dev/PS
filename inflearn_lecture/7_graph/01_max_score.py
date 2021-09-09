# 210907
# 210909 다시 풀음.
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = list(map(int, input().split()))

    def dfs(current=0, remain=M, last=0):
        if remain < 0:
            return 0
        if last == N:
            return current
        score, time = problem_list[last]
        return max(
            current,
            dfs(current + score, remain - time, last + 1),
            dfs(current, remain, last + 1)
        )

    problem_list = []
    for _ in range(N):
        problem_list.append(list(map(int, input().split())))

    return [[str(dfs())]]

if __name__ == "__main__":
    print(solution(examine=True))


