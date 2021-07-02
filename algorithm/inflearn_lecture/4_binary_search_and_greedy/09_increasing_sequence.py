# 210702
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    _ = input()
    seq, result = list(map(int, input().split())), ''
    start, end, prev = 0, len(seq) - 1, 0
    while prev < max(seq[start], seq[end]):  # 이전의 수가 1)큰 것보다 큰 경우
        # 2)작은 것보다 작은 경우
        if prev < min(seq[start], seq[end]):
            prev, temp = min((seq[start], 'L'), (seq[end], 'R'))
        else:  # 3)큰 것보다 작은 경우
            prev, temp = max((seq[start], 'L'), (seq[end], 'R'))

        if temp == "L":
            start += 1
        else:
            end -= 1
        result += temp

    return [[str(len(result))], [str(result)]]

if __name__ == "__main__":
    print(solution(examine=True))