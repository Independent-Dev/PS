from examine import examine
import sys, math

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(x=1, count=1, arr=[]):
        if count > M:
            answer.append(' '.join(arr))
        else:
            for i in range(x, N - M + count + 1):
                dfs(i + 1, count + 1, arr + [str(i)])

    N, M = [int(x) for x in input().split()]
    answer = []
    dfs()

    return answer + [str(len(answer))]


if __name__ == "__main__":
    print(solution(examine=True))
