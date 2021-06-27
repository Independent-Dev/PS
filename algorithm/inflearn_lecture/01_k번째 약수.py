import sys, os
from examine import examine
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# count, start = 0, 0
#
# while count != k:
#     start += 1
#     if start > n:
#         print(-1)
#         break
#     if n % start == 0:
#         count += 1
# else:
#     print(start)

@examine
def solution(input_args):
    n, k = map(int, input_args[0].split())
    count, start = 0, 0
    while count != k:
        start += 1
        if start > n:
            return str(-1)
            break
        if n % start == 0:
            count += 1
    else:
        return str(start)

if __name__ == "__main__":
    solution("x")