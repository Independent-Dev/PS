from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    coin_list = [int(num) for num in input().split()]
    target = int(input())
    visited = [0] * (target + 1)
    count = 1
    position_list = [0]
    while not visited[target]:
        temp = []
        for position in position_list:
            for coin in coin_list:
                next = coin + position
                if next == target:
                    return [str(count)]
                if next < target and not visited[next]:
                    visited[next] = 1
                    temp.append(next)
        position_list = temp[:]
        count += 1


if __name__ == "__main__":
    print(solution(examine=True))
