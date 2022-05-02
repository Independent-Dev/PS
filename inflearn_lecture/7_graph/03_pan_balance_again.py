from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(idx=0, count=0):
        if idx == N:
            calculated[abs(count)] = 0
        else:
            dfs(idx + 1, count + arr[idx])
            dfs(idx + 1, count - arr[idx])
            dfs(idx + 1, count)

    N = int(input())

    arr = [int(x) for x in input().split()]
    calculated = [1] * (sum(arr) + 1)

    dfs()
    return [str(sum(calculated))]

if __name__ == "__main__":
    print(solution(examine=True))
