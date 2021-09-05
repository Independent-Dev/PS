# 210905 gold4
import sys
from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(n, c):
    result_list = [sys.maxsize] * (n + 1)
    result_list[c] = 0  # 왜 이걸 빼면 valueError가 나나...??
    q = [(0, c)]
    while q:
        cost, start = heappop(q)
        if cost <= result_list[start]:
            for e, c in graph[start]:
                c += cost
                if c < result_list[e]:
                    result_list[e] = c
                    heappush(q, (c, e))
    infected_computer = [r for r in result_list if r != sys.maxsize]
    return len(infected_computer), max(infected_computer)

input = sys.stdin.readline
result = []

testcase_count = int(input().strip())
for _ in range(testcase_count):
    n, d, c = list(map(int, input().strip().split()))
    graph = defaultdict(list)
    
    for _ in range(d):
        a, b, s = list(map(int, input().strip().split()))
        graph[b].append((a, s))
    result.append(list(dijkstra(n, c)))

for count, cost in result:
    print(count, cost)
    
