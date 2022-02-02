import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    MAX = 0
    for _ in range(N):
        temp = [int(x) for x in input().split()]
        set_temp = set(temp)
        if len(set_temp) == 3:
            prize = max(temp) * 100
        elif len(set_temp) == 2:
            # pop_item = temp.pop()
            # same = pop_item if pop_item in temp else (set_temp - set([pop_item])).pop()
            same = sum(set_temp) - (temp[0] ^ temp[1] ^ temp[2])
            prize = 1000 + 100 * same
        else:
            prize = 10000 + 1000 * set_temp.pop()
        MAX = max(MAX, prize)

    return [str(MAX)]

if __name__ == "__main__":
    print(solution(examine=True))