# 2109013
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(current = 0, next=0):
        if current > target:
            return
        if current == target:
            nonlocal count
            count += 1
            return
        if next == len(coin_list):
            return
        for i in range(coin_list[next][1] + 1):
            dfs(current + coin_list[next][0] * i, next + 1)

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    
    target = int(input())
    coin_list = []
    count = 0
    for _ in range(int(input())):
        coin_list.append(list(map(int, input().split())))
    
    dfs()

    return [[str(count)]]

if __name__ == "__main__":
    print(solution(examine=True))


