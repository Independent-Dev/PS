from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N, K = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    count = 0
    idx = N
    MAX = 100
    for i, a in enumerate(arr):
        if a > arr[K]:
            count += 1
            if a <= MAX:
                MAX = a
                idx = i

    return [str(count + len([x for i, x in enumerate(arr) if x == arr[K] and ((i <= K or i > idx) if idx > K else (idx < i <= K))]))]

if __name__ == "__main__":
    print(solution(examine=True))