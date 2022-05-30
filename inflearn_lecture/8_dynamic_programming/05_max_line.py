from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    target = {int(number): idx + 1 for idx, number in enumerate(input().split())}
    res = [0] * N

    for i in range(1, N + 1):
        res[target[i] - 1] = max(res[:target[i]]) + 1

    return [str(max(res))]

if __name__ == "__main__":
    print(solution(examine=True))
