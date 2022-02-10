import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    res = 0
    for i in range(N):
        temp = 0
        for j in arr[i:]:
            temp += j
            if temp == M:
                res += 1
                break
            elif temp > M:
                break
    return [str(res)]

if __name__ == "__main__":
    print(solution(examine=True))