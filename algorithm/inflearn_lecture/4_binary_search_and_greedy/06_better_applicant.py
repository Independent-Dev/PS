# 210702
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    all_applicants = []

    for _ in range(int(input())):
        all_applicants.append(list(map(int, input().split())))

    all_applicants.sort(reverse=True)

    count, prev_point = 1, all_applicants[0][1]
    for _, current_point in all_applicants[1:]:
        if current_point > prev_point:
            prev_point = current_point
            count += 1
    return [str(count)]


if __name__ == "__main__":
    print(solution(examine=True))