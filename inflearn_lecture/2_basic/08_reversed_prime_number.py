import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    arr = [int(inp[::-1]) for inp in input().split()]
    prime_number_list = []
    for e in arr:
        if e >= 2:
            for i in range(2, e):
                if e % i == 0:
                    break
            else:
                prime_number_list.append(e)

    return [str(e) for e in prime_number_list]

if __name__ == "__main__":
    print(solution(examine=True))