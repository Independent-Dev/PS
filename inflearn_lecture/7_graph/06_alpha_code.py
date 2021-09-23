# 210923
from examine.examine import examine
import sys, string
alphabet_dict = {str(i) : word for i, word in enumerate(string.ascii_uppercase, start=1)}

@examine
def solution(**kwargs):
    def dfs(arr = [], next=0):
        if next == len_alpha_code:
            result.append(''.join(arr))
            return
            
        if alpha_code[next] != '0':
            dfs(arr + [alphabet_dict[alpha_code[next]]], next + 1)
        if next + 1 < len_alpha_code and alpha_code[next : next + 2] in alphabet_dict:
            dfs(arr + [alphabet_dict[alpha_code[next : next + 2]]], next + 2)


    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    
    alpha_code = input()
    len_alpha_code = len(alpha_code)
    result = []

    dfs()

    result.append(str(len(result)))

    return [[r] for r in result]

if __name__ == "__main__":
    print(solution(examine=True))
