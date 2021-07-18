# 210718
from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    prince, num = map(int, input().split())
    i, result = 0, [n for n in range(1, prince + 1)]
    num -= 1
    for _ in range(prince - 1):
        i += num
        del result[i % prince]
        i %= prince
        prince -= 1
    return [[str(result[0])]]

if __name__ == "__main__":
    print(solution(examine=True))
