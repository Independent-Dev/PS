from examine import examine
import sys

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(y, x):
        nonlocal target_y, target_x
        if y == target_y and x == target_x:
            from pprint import pprint
            pprint(visited)
            nonlocal count
            count += 1
        else:
            for dir_y, dir_x in direction:
                next_y, next_x = y + dir_y, x + dir_x
                if 0 <= next_y < N and 0 <= next_x < N and \
                        not visited[next_y][next_x] and mountain[next_y][next_x] > mountain[y][x]:
                    visited[next_y][next_x] = 1
                    dfs(next_y, next_x)
                    visited[next_y][next_x] = 0

    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    N = int(input())

    mountain = []

    for i in range(N):
        mountain.append([int(num) for num in input().split()])

    visited = [[0] * N for _ in range(N)]

    start_x, start_y = 0, 0
    target_x, target_y = 0, 0
    MIN, MAX = mountain[0][0], mountain[0][0]

    for i, height_list in enumerate(mountain):
        for j, height in enumerate(height_list):
            if height > MAX:
                MAX = height
                target_y, target_x = i, j

            if height < MIN:
                MIN = height
                start_y, start_x = i, j

    print(f"start_x: {start_x}, start_y: {start_y}, MIN: {MIN}")
    print(f"target_x: {target_x}, target_y: {target_y}, MAX: {MAX}")

    visited[start_y][start_x] = 1
    count = 0
    dfs(start_y, start_x)

    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=True))
