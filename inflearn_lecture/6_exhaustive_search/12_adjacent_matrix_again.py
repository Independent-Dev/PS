from examine import examine
import sys, pprint

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')



    N, M = [int(x) for x in input().split()]
    matrix = [[0] * N for _ in range(N)]
    for _ in range(M):
        x, y, w = [int(x) for x in input().split()]
        matrix[x-1][y-1] = w

    return matrix


if __name__ == "__main__":
    pprint.pprint(solution(examine=False))
