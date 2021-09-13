# 2109013
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(current_profit = 0, next=0):
        if next > day_count:
            return 0
        if next == day_count:
            return current_profit
        return max(
            current_profit,
            dfs(current_profit, next + 1),
            dfs(current_profit + counsel_list[next][1], next + counsel_list[next][0])
        )

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    counsel_list = []
    day_count = int(input())
    for _ in range(day_count):
        counsel_list.append(list(map(int, input().split())))

    return [[str(dfs())]]

if __name__ == "__main__":
    print(solution(examine=True))


