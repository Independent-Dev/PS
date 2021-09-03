# 210903
from examine.examine import examine
import sys, pprint

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    N, M = list(map(int, input().split()))
    adjacent_matrix = [[0] * N for _ in range(N)]
    for _ in range(M):
        row, col, val = list(map(int, input().split()))
        adjacent_matrix[row - 1][col - 1] = val

    return adjacent_matrix

if __name__ == "__main__":
    pprint.pprint(solution(examine=False))


