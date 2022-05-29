from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def DFS(N):
        if N <= 2:
            return N

        if not res_list[N]:
            res_list[N] = DFS(N - 1) + DFS(N - 2)
        return res_list[N]


    N = int(input())
    res_list = [0] * (N + 1)

    return [str(DFS(N))]

if __name__ == "__main__":
    print(solution(examine=True))