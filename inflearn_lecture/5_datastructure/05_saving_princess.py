# 210718
from examine import examine
from collections import deque
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    prince, num = map(int, input().split())
    i, result = 0, list(range(1, prince + 1))
    num -= 1
    # teacher sol. 속도 면에서 이게 더 빠를 것 같다 del list는 O(n)이 걸리므로.
    result = deque(result)
    while len(result) != 1:
        for _ in range(num):
            n = result.popleft()
            result.append(n)
        _ = result.popleft()
    
    # mysol
    # for _ in range(prince - 1):
    #     i += num
    #     del result[i % prince]
    #     i %= prince
    #     prince -= 1
    return [[str(result[0])]]

if __name__ == "__main__":
    print(solution(examine=True))
