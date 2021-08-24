import sys
from collections import defaultdict

from examine.examine import examine


@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    
    N, M = map(int, input().split())

    res_dict = defaultdict(int)
    for n in range(1, N + 1):
        for m in range(1, M + 1):
            res_dict[n + m] += 1
    
    MAX, res_list = 0, list()
    for key, val in res_dict.items():
        if val > MAX:
            MAX, res_list = val, [key]
        elif val == MAX:
            res_list.append(key)

            
    return [list(map(str, res_list))]

if __name__ == "__main__":
    print(solution(examine=True))