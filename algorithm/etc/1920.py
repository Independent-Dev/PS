import sys

input = sys.stdin.readline

N = int(input().strip())
target = set([int(num) for num in input().split()])
M = int(input().strip())
exp = [int(num) for num in input().split()]

for e in exp:
    if e in target:
        print(1)
    else:
        print(0)