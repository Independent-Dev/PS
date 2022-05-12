from examine import examine
import sys

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    maze = []
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for _ in range(7):
        maze.append([int(num) for num in input().split()])

    pos_list = [(0, 0)]
    maze[0][0] = 1
    count = 0
    while (6, 6) not in pos_list:
        next_pos = []
        for pos_y, pos_x in pos_list:
            for dir_y, dir_x in direction:
                next_y, next_x = pos_y + dir_y, pos_x + dir_x
                if 0 <= next_y <=6 and 0 <= next_x <= 6 and not maze[next_y][next_x]:
                    next_pos.append((next_y, next_x))
                    maze[next_y][next_x] = 1
        if next_pos:
            pos_list = next_pos
            count += 1
        else:
            count = -1
            break

    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=True))
