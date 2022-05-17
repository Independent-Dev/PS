from examine import examine
import sys, pprint

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    direction = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    N = int(input())
    count = 0

    island = []
    height_list = []


    for i in range(N):
        island.append([int(num) for num in input().split()])
        height_list.extend(island[-1][:])

    height_list = sorted(list(set(height_list)))

    max_count = 0
    for height in height_list:
        count = 0
        visited = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if not visited[y][x] and island[y][x] - height > 0:
                    count += 1
                    island_list = [(y, x)]
                    visited[y][x] = 1
                    while island_list:
                        temp_list = []
                        for island_y, island_x in island_list:
                            for dir_y, dir_x in direction:
                                next_y, next_x = island_y + dir_y, island_x + dir_x
                                if 0 <= next_y < N and 0 <= next_x < N and island[next_y][next_x] - height > 0 and not visited[next_y][next_x]:
                                    visited[next_y][next_x] = 1
                                    temp_list.append((next_y, next_x))
                        island_list = temp_list
        max_count = max(max_count, count)

    return [str(max_count)]

if __name__ == "__main__":
    print(solution(examine=True))
