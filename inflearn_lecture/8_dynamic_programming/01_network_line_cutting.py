from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    first, second = 1, 2
    for _ in range(N - 2):
        first, second = second, second + first

    return [str(second)]

if __name__ == "__main__":
    print(solution(examine=True))
