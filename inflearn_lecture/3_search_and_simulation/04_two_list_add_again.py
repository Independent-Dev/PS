import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    arr_n = [int(x) for x in input().split()]
    M = int(input())
    arr_m = [int(x) for x in input().split()]

    count_n = count_m = 0
    result = []
    while count_n < N and count_m < M:
        if arr_n[count_n] < arr_m[count_m]:
            result.append(arr_n[count_n])
            count_n += 1
        else:
            result.append(arr_m[count_m])
            count_m += 1

    result.extend(arr_n[count_n:])
    result.extend(arr_m[count_m:])

    return [' '.join(str(x) for x in result)]

if __name__ == "__main__":
    print(solution(examine=True))