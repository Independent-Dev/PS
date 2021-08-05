# 210727
from examine import examine
import sys

def to_binary_format(n):
    if n == 1:
        return n
    return str(to_binary_format(n // 2)) + str(n % 2)

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    
    N = int(input())
    return [[to_binary_format(N)]]

if __name__ == "__main__":
    print(solution(examine=True))
