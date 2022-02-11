import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    MAX = 0
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append([int(x) for x in input().split()])

    MAX = max(MAX, *[sum(l) for l in arr])  # 가로합
    MAX = max(MAX, *[sum(l) for l in list(zip(*arr))])  # 세로합
    MAX = max(MAX, sum(arr[i][i] for i in range(N)), sum(arr[i][N - 1 - i] for i in range(N)))  # 대각선 합
    return [str(MAX)]

if __name__ == "__main__":
    print(solution(examine=True))