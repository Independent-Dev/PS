# 210612, silver 4

import sys
input = sys.stdin.readline

N, M = [int(num) for num in input().split()]
can_not_see = ['' for _ in range(N)]
can_not_hear = ['' for _ in range(M)]

for n in range(N):
    can_not_see[n] = input().strip()

for m in range(M):
    can_not_hear[m] = input().strip()

can_not_see_or_hear = set(can_not_see) & set(can_not_hear)

print(len(can_not_see_or_hear))
for name in sorted(list(can_not_see_or_hear)):
    print(name)
