from examine import examine
import sys, math

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    
    num = int(input())
    arr = list(map(int, input().split()))
    average = round(sum(arr) / num)

    res_num, res_index, gap = -math.inf, -1, math.inf
    for ind, el in enumerate(arr, start=1):
        temp_gap = abs(average - el)
        if temp_gap < gap or (temp_gap == gap and el > res_num):
            res_num, res_index, gap = el, ind, temp_gap

            
    return [[str(average), str(res_index)]]

if __name__ == "__main__":
    print(solution(examine=True))
