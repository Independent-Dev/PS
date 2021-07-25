# 210726
import sys
from examine import examine 

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    target = input().strip()
    cnt = int(input().strip())
    arr = [input().strip() for _ in range(cnt)]
    res = []
    for i, s in enumerate(arr, start=1):
        temp_cnt = 0
        flag = False
        for w in s:
            if target.find(w) == temp_cnt:
                temp_cnt += 1
            elif target.find(w) > temp_cnt:
                break
            if temp_cnt == len(target):
                flag = True
                break
        if flag:
            res.append([f"#{i}", "YES"])
        else:
            res.append([f"#{i}", "NO"])
    return res

if __name__ == "__main__":
    print(solution(examine=True))