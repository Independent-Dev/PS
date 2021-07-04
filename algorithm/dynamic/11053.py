# 210704 silver2
# dp

# 내 풀이
def lis(arr):
    arr = [0] + arr
    N = len(arr)
    cache = [-1] * N

    def find(start):
        if cache[start] != -1:
            return cache[start]
        res = 0
        for i in range(start + 1, N):
            if arr[start] < arr[i]:
                res = max(res, find(i) + 1)

        cache[start] = res
        return res

    return find(0)

N = int(input())
arr = list(map(int, input().split()))
print(lis(arr))
이
# 준호 풀
dp = [1] * N

for i in range(1, N):
    for j in range(1, i+1):
        if arr[i] > arr[i - j]:
            dp[i] = max(dp[i], dp[i - j] + 1)

print(max(dp))


