import sys
from examine import examine

@examine
def solution(*args):
    result = []
    for i in range(0, int(args[0][0][0]), 2):
        N, s, e, q = map(int, args[0][i+1])
        result.append(sorted(list(map(int, args[0][i+2][s-1:e])))[q-1])
    return result

if __name__ == "__main__":
    solution()

else:
    for _ in range(int(input())):
        N, s, e, q = map(int, input().split())
        print(sorted(list(map(int, input().split()[s-1:e])))[q-1])
