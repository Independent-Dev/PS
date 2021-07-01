from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    K, N = map(int, input().split())
    lan_length = [int(input()) for _ in range(K)]
    result = 0
    start, stop = 0, max(lan_length)
    while start <= stop:
        mid = (start + stop) // 2
        if sum(x // mid for x in lan_length) >= N:
            result = max(mid, result)
            start = mid + 1
        else:
            stop = mid - 1
    return [str(result)]

if __name__ == "__main__":
    print(solution(examine=True))