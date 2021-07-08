# 210702
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    _ = input()
    box_size_list = sorted(list(map(int, input().split())))

    for _ in range(int(input())):
        box_size_list[0] += 1
        box_size_list[-1] -= 1
        i = 1
        while i < len(box_size_list) and box_size_list[i] < box_size_list[i - 1]:
            box_size_list[i], box_size_list[i - 1] = box_size_list[i - 1], box_size_list[i]
            i += 1

        j = -2
        while j >= -len(box_size_list) and box_size_list[j] > box_size_list[j + 1]:
            box_size_list[j], box_size_list[j + 1] = box_size_list[j + 1], box_size_list[j]
            j -= 1

    return [str(box_size_list[-1] - box_size_list[0])]


if __name__ == "__main__":
    print(solution(examine=True))