# 210924
from examine.examine import examine
import sys

JUMP_LIST = [-1, 1, 5]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    result = 0
    S, E = list(map(int, input().split()))
    visited = [0] * (2 * max(S, E) - min(S, E))

    curr_list = [S]
    visited[S] = 1
    while not visited[E]:
        result += 1
        temp = set()
        for curr in curr_list:
            for JUMP in JUMP_LIST:
                next = curr + JUMP
                if len(visited)> next >= 1 and not visited[next]:
                    temp.add(next)
                    visited[next] = 1
        curr_list = list(temp)

    return [[str(result)]]

if __name__ == "__main__":
    print(solution(examine=True))
