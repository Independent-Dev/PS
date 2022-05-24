from examine import examine
import sys
from itertools import combinations

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, M = [int(num) for num in input().split()]
    city_map = []
    house_list = []
    pizza_store_list = []
    pizza_distance_list = []

    for y in range(N):
        city_map.append([int(num) for num in input().split()])
        for x in range(N):
            if city_map[-1][x] == 1:
                house_list.append([y, x])
            elif city_map[-1][x] == 2:
                pizza_store_list.append([y, x])

    for house_y, house_x in house_list:
        pizza_distance_list.append({})
        for idx, (pizza_store_y, pizza_store_x) in enumerate(pizza_store_list):
            pizza_distance_list[-1][idx] = abs(house_y - pizza_store_y) + abs(house_x - pizza_store_x)

    result = 2 * N * len(house_list)

    for pizza_store_com in list(combinations(range(len(pizza_store_list)), M)):
        temp = 0
        for pizza_distance in pizza_distance_list:
            min_distance = N + N
            for pizza_store in pizza_store_com:
                min_distance = min(min_distance, pizza_distance[pizza_store])
            temp += min_distance
        result = min(temp, result)

    return [str(result)]

if __name__ == "__main__":
    print(solution(examine=True))
