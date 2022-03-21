# 210727
from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(x=1, res=''):
        if x > N:
            if res:
                arr.append(' '.join(list(res)))
        else:
            dfs(x + 1, res + str(x))
            dfs(x + 1, res)

    N = int(input())
    arr = []
    dfs()

    return arr


if __name__ == "__main__":
    print(solution(examine=True))
