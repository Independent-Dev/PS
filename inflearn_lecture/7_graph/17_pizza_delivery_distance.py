from examine import examine
import sys, pprint

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(idx=0, city_pizza_distance=0):
        nonlocal result
        if not result:
            if idx == len(house_list):
                if sum(visited) <= M:
                    result = city_pizza_distance
            else:
                for distance, pizza_store_idx in pizza_distance_list[idx]:
                    visited[pizza_store_idx] = 1
                    dfs(idx + 1, city_pizza_distance + distance)
                    visited[pizza_store_idx] = 0


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

    visited = [0] * len(pizza_store_list)

    for house_y, house_x in house_list:
        pizza_distance_list.append([])
        for idx, (pizza_store_y, pizza_store_x) in enumerate(pizza_store_list):
            pizza_distance_list[-1].append([abs(house_y - pizza_store_y) + abs(house_x - pizza_store_x), idx])
        pizza_distance_list[-1].sort()

    result = None

    dfs()
    return [str(result)]

if __name__ == "__main__":
    print(solution(examine=True))
