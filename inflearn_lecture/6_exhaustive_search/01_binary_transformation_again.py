from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    target = int(input())
    res = ''
    while target:
        res = str(target % 2) + res
        target //= 2

    return [res]

if __name__ == "__main__":
    print(solution(examine=False))