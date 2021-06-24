# dijkstra algorithm example
# 출처: <이것이 취업을 위한 코딩 테스트다>(나동빈, 한빛 미디어) 248page. 일부 코드 수정

import heapq
INF = int(1e9)

V, E = map(int, input().split())  # V: 노드의 개수, E: 간선의 개수
root = int(input())  # 시작 노드 번호
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def dijkstra(root):
    q = []
    heapq.heappush(q, (0, root))
    distance[root] = 0
    while q:
        dist, now = heapq.heappop(q)
        # TODO 이 조건문을 어떻게 좀 수정하고 싶은데....
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
