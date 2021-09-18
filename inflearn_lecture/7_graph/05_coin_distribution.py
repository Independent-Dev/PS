# 210918
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    def dfs(a=0, b=0, c=0, next=0):
        if next == coin_number:
            if a!=b and b!=c and a!=c:
                all_result_list.append([a, b, c])
            return
        dfs(a + coin_list[next], b, c, next + 1)
        dfs(a, b + coin_list[next], c, next + 1)
        dfs(a, b, c + coin_list[next], next + 1)

    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    
    coin_number = int(input())
    coin_list = []

    for _ in range(coin_number):
        coin_list.append(int(input()))
    
    all_coin_sum = sum(coin_list)
    all_result_list = []
    min_gap = sys.maxsize

    dfs()
    for result in all_result_list:
        min_in_result, max_in_result = min(result), max(result)
        min_gap = min(min_gap, max_in_result - min_in_result)
            

    return [[str(min_gap)]]

if __name__ == "__main__":
    print(solution(examine=True))

# 경우의 수를 어떻게 줄일 것인가. itertools에 있을 것 같기는 한데 이건 그렇게 푸는 문제가 아니다...


