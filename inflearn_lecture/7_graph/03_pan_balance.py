# 210914
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(current_sum = 0, next=0):
        if current_sum >= 0:
            number_of_case[current_sum] = 0
        if next == K:
            return
        for i in range(-1, 2):
            dfs(current_sum + (i * pendulum_list[next]), next + 1)

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    K = int(input())
    pendulum_list = list(map(int, input().split()))
    number_of_case = [1] * (sum(pendulum_list) + 1)

    dfs()

    return [[str(sum(number_of_case))]]

if __name__ == "__main__":
    print(solution(examine=True))