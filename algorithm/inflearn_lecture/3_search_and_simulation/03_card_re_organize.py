from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    target = [num for num in range(1, 21)]
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    for _ in range(10):
        start, stop = map(int, input().split())
        target[start - 1:stop] = target[start - 1:stop][::-1]
    return list(map(str, target[:]))

if __name__ == "__main__":
    print(solution(examine=True))