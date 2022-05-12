from examine import examine
import sys

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(x = 0, y = 0):
        if x == 6 and y == 6:
            nonlocal count
            count += 1
        for dir_y, dir_x in direction:
            next_y, next_x = y + dir_y, x + dir_x
            if 0 <= next_y <= 6 and 0 <= next_x <= 6 and not maze[next_y][next_x]:
                maze[next_y][next_x] = 1
                dfs(next_x, next_y)
                maze[next_y][next_x] = 0

    maze = []
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for _ in range(7):
        maze.append([int(num) for num in input().split()])

    maze[0][0] = 1
    count = 0
    dfs()

    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=False))
