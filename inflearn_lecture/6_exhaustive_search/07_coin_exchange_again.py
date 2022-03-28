# 220328
from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    _ = input()
    arr = [int(x) for x in input().split()]
    target = int(input())
    visited = [False] * (target + 1)
    count, queue = 0, [0]
    while not visited[target]:
        count += 1
        temp = []
        for q in queue:
            for a in arr:
                next = q + a
                if next <= target and not visited[next]:
                    temp.append(next)
                    visited[next] = True
        queue = temp

    return [str(count)]


if __name__ == "__main__":
    print(solution(examine=True))
