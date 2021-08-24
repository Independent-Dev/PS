# 210824 이건 어떻게 푸는 건지 모르겠다....
# 힌트 얻어서 풀긴 했는데 대충대충 푼 느낌이다... 좀 찝찝하다... 나중에 다시 지웠다가 풀어보는 것으로!!
# path와 리스트 합치기 같은 거...

from examine.examine import examine
import sys

def DFS(n, target, temp_str=[]):
    if n > target:
        if temp_str:
            return [temp_str]
        else:
            return []
    else:
        return DFS(n + 1, target, temp_str + [str(n)]) + DFS(n + 1, target, temp_str)
        

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    
    target = int(input())
    return list(DFS(1, target))

if __name__ == "__main__":
    print(solution(examine=True))