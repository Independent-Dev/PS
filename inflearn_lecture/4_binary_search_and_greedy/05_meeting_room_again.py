import sys, math
from examine.examine import examine

# 참조
# 해법: https://source-sc.tistory.com/59
# 여러 기준 정렬: https://dailyheumsi.tistory.com/67


@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    room_list = []
    N = int(input())
    for _ in range(N):
        room_list.append([int(x) for x in input().split()])
    room_list.sort(key=lambda x:(x[1], -x[0]))
    count = 1

    prev_time = room_list.pop(0)
    for time in room_list:
        if prev_time[1] <= time[0]:
            prev_time = time
            count += 1

    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=True))