# 211009 거짓말
# gold4

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
cur = M

knowing_people =list(map(int, input().split()))

party_people = list()

for _ in range(M):
    party_people.append(set(map(int, input().split()[1:])))

visited = [0] * len(party_people)

if len(knowing_people) == 1:
    print(M)
else:
    knowing_people = set(knowing_people[1:])
    while cur:
        cur = 0
        for i, people in enumerate(party_people):
            if not visited[i] and people & knowing_people:
                knowing_people |= people
                cur += 1
                visited[i] = 1
    print(M - sum(visited))