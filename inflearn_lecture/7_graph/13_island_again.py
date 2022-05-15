from examine import examine
import sys, pprint

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    direction = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
    N = int(input())
    count = 0

    island = []

    for i in range(N):
        island.append([int(num) for num in input().split()])

    for y in range(N):
        for x in range(N):
            if island[y][x]:
                count += 1
                island_list = [(y, x)]
                island[y][x] = 0
                while island_list:
                    temp_list = []
                    for island_y, island_x in island_list:
                        for dir_y, dir_x in direction:
                            next_y, next_x = island_y + dir_y, island_x + dir_x
                            if 0 <= next_y < N and 0 <= next_x < N and island[next_y][next_x]:
                                island[next_y][next_x] = 0
                                temp_list.append((next_y, next_x))
                    island_list = temp_list

    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=True))
