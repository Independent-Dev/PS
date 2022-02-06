import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    answer = []
    for i in range(1, N + 1):
        inp = input().lower()
        answer.append(f"#{i} {'YES' if inp == inp[::-1] else 'NO'}")

    return answer

if __name__ == "__main__":
    print(solution(examine=True))