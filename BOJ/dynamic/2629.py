# 210914
# 양팔저울 gold2
def dfs(current_sum = 0, next=0):
    new = abs(current_sum)
    number_of_case[new] = 0
    if next == K:
        return 0
    if not visited[next][new]:
        for i in range(-1, 2):
            dfs(current_sum + (i * pendulum_list[next]), next + 1)
        visited[next][new] = 1

K = int(input())
pendulum_list = list(map(int, input().split()))
target_number = int(input())
target_list = list(map(int, input().split()))

number_of_case = [1] * (sum(pendulum_list) + 1)
visited = [[0] * (sum(pendulum_list) + 1) for _ in range(K)]

dfs()

for target in target_list:
    print("N" if number_of_case[target] else "Y", end=" ")