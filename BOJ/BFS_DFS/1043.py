# 211009 거짓말
# gold4

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
prev, cur = M, 0

knowing_people =list(map(int, input().split()))

party_people = list()

for _ in range(M):
    party_people.append(set(map(int, input().split()[1:])))

if len(knowing_people) == 1:
    print(M)
else:
    knowing_people = set(knowing_people[1:])
    while prev != cur:
        prev = cur
        cur = 0
        for people in party_people:
            if people & knowing_people:
                knowing_people |= people
                cur += 1
    print(M - cur)