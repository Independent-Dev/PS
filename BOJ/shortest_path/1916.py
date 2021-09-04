# 210904
# 왜 메모리 이슈가 생겼던 것인지 아직 완벽히 이해하지는 못하겠음. 
import heapq, sys

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)

bus_dict = dict()
result_list = [INF] * (N + 1)

for _ in range(M):
    start, end, cost = list(map(int, input().split()))
    if start not in bus_dict.keys():
        bus_dict[start] = [(cost, end)]
    else:
        bus_dict[start].append((cost, end))

departure, destination = list(map(int, input().split()))

temp = [(0, departure)]

while temp:
    cost, start = heapq.heappop(temp)
    if result_list[start] < cost:
        continue
    if start in bus_dict:
        for c, e in bus_dict[start]:
            c += cost 
            if c < result_list[e]:
                result_list[e] = c
                heapq.heappush(temp, (c, e))

print(result_list[destination])

# while departure != destination:
#     if departure in bus_dict.keys():
#         for c, e in bus_dict[departure]:
#             if result_list[e - 1] == 0:
#                 heapq.heappush(temp, (result_list[departure - 1] + c, e))
#     cost, end = heapq.heappop(temp)
    
#     result_list[end - 1] = cost
#     departure = end


