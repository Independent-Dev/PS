from examine import examine
import sys, math

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, limit = [int(num) for num in input().split()]
    knapsack = [0] * (limit + 1)
    for i in range(N):
        weight, price = [int(num) for num in input().split()]
        for i in range(weight, len(knapsack)):
            knapsack[i] = max(knapsack[i - weight] + price, knapsack[i])

    return [str(knapsack[-1])]

if __name__ == "__main__":
    print(solution(examine=True))
