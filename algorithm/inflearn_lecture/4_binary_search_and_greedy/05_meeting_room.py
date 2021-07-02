# 210701
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    all_meetings = []

    for _ in range(int(input())):
        all_meetings.append(list(map(int, input().split())))

    all_meetings.sort(key=lambda el: el[1])
    possible_meetings = [all_meetings[0][1]]
    for start, end in all_meetings[1:]:
        if possible_meetings[-1] <= start:
            possible_meetings.append(end)

    return [str(len(possible_meetings))]


if __name__ == "__main__":
    print(solution(examine=True))