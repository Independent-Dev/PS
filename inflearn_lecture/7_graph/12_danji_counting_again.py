from examine import examine
import sys, pprint

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    N = int(input())
    count = []

    danji = []

    for i in range(N):
        danji.append([int(num) for num in list(input())])

    for y in range(N):
        for x in range(N):
            if danji[y][x]:
                count.append(1)
                house_list = [(y, x)]
                danji[y][x] = 0
                while house_list:
                    temp_list = []
                    for house_y, house_x in house_list:
                        for dir_y, dir_x in direction:
                            next_y, next_x = house_y + dir_y, house_x + dir_x
                            if 0 <= next_y < N and 0 <= next_x < N and danji[next_y][next_x]:
                                count[-1] += 1
                                danji[next_y][next_x] = 0
                                temp_list.append((next_y, next_x))
                    house_list = temp_list


    return [str(len(count))] + [str(x) for x in sorted(count)]

if __name__ == "__main__":
    print(solution(examine=True))
