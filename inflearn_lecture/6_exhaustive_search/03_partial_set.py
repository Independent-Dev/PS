# 210824 이건 어떻게 푸는 건지 모르겠다....
# 힌트 얻어서 풀긴 했는데 대충대충 푼 느낌이다... 좀 찝찝하다... 나중에 다시 지웠다가 풀어보는 것으로!!
# 사실 이게 문자열 문제와 굉장히 비슷했는데 이걸 풀지 못했군...
# path와 리스트 합치기 같은 거...

from examine.examine import examine
import sys


@examine
def solution(**kwargs):
    def DFS(n, temp_str=''):
        if n > target:
            if temp_str:
                return res.append(list(temp_str))
        else:
            DFS(n + 1, temp_str + str(n))
            DFS(n + 1, temp_str)
            
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    
    target = int(input())
    res = []
    DFS(1)
    return res

if __name__ == "__main__":
    print(solution(examine=True))