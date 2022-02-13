import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def count_album(limit):
        count = 1
        temp = 0
        for a in arr:
            temp += a
            if temp > limit:
                count += 1
                temp = a
        return count

    def binary_search(start, end):
        if start == end:
            if count_album(start) > M:
                start += 1
            return start

        limit = (start + end) // 2
        count = count_album(limit)
        if count <= M:
            return binary_search(start, limit - 1)
        else:
            return binary_search(limit + 1, end)

    N, M = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    return [str(binary_search(max(arr), sum(arr)))]

if __name__ == "__main__":
    print(solution(examine=True))