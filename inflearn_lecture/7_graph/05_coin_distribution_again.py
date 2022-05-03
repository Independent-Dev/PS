from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(idx=0):
        if idx == N:
            nonlocal res
            # if people[0] != people[1] != people[2] != people[0]:
            if (people[0] ^ people[1] ^ people[2]) not in people:
                res = min(max(people) - min(people), res)
        else:
            for i in range(3):
                people[i] += coin[idx]
                dfs(idx + 1)
                people[i] -= coin[idx]

    N = int(input())

    coin = []
    people = [0] * 3

    for _ in range(N):
        coin.append(int(input()))

    res = sum(coin)
    dfs()
    return [str(res)]

if __name__ == "__main__":
    print(solution(examine=True))
