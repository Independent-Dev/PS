# 210702
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    _ = input()
    box_height_list = [int(num) for num in input().split()]
    MIN, MAX = min(box_height_list), max(box_height_list)
    change_count = int(input())

    box_height_count_list = [0] * (MAX + 1)
    for height in box_height_list:
        box_height_count_list[height] += 1

    for _ in range(change_count):
        box_height_count_list[MIN] -= 1
        box_height_count_list[MIN + 1] += 1

        if box_height_count_list[MIN] == 0:
            MIN += 1

        box_height_count_list[MAX] -= 1
        box_height_count_list[MAX - 1] += 1

        if box_height_count_list[MAX] == 0:
            MAX -= 1

        if MIN > MAX:
            MAX, MIN = MIN, MAX

    return [str(MAX - MIN)]


if __name__ == "__main__":
    print(solution(examine=True))