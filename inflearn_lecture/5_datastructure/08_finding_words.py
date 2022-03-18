from examine.examine import examine
import sys
from collections import defaultdict

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    words = defaultdict(int)
    N = int(input())
    for _ in range(N):
        words[input()] += 1

    for _ in range(N - 1):
        words[input()] -= 1

    return [key for key, value in words.items() if value]

if __name__ == "__main__":
    print(solution(examine=True))