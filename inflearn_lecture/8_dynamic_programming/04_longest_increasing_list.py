from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    target = [int(number) for number in input().split()]
    res = [0] * N

    for i in range(N):
        res[i] = max([res[j] if target[j] < target[i] else 0 for j in range(i + 1)]) + 1

    return [str(max(res))]

if __name__ == "__main__":
    print(solution(examine=True))
