import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
index_dict = {}
for i, a in enumerate(sorted(list(set(arr)))):
    index_dict[a] = i

for a in arr:
    print(index_dict[a], end=' ')