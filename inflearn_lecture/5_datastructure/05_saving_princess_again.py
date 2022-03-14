from examine.examine import examine
import sys
from collections import deque

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, K = [int(x) for x in input().split()]
    queue = deque([x for x in range(1, N + 1)])
    for _ in range(N - 1):
        for _ in range(K - 1):
            queue.append(queue.popleft())
        queue.popleft()

    return [str(queue[0])]

if __name__ == "__main__":
    print(solution(examine=True))