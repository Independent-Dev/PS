from examine import examine
import sys, math

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, limit = [int(num) for num in input().split()]
    jewelry_list = []
    for i in range(N):
        jewelry_list.append([int(num) for num in input().split()])

    knapsack = [0] * (limit + 1)
    for i in range(1, len(knapsack)):
        for weight, price in jewelry_list:
            if i >= weight:
                knapsack[i] = max(knapsack[i - weight] + price, knapsack[i])

    return [str(knapsack[-1])]

if __name__ == "__main__":
    print(solution(examine=True))
