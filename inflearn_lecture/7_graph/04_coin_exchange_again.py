from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(idx=0, price=0):
        if price == target:
            nonlocal count
            count += 1
        elif price < target and idx < N:
            for coin_num in range(arr[idx][1] + 1):
                dfs(idx + 1, price + arr[idx][0] * coin_num)

    target = int(input())
    N = int(input())

    arr = []

    for _ in range(N):
        arr.append([int(x) for x in input().split()])

    count = 0
    dfs()
    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=True))
