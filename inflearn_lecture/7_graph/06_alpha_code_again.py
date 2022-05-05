from examine import examine
import sys, string

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def dfs(idx=0, result_str=''):
        if idx >= len(target_str):
            code.append(result_str)
        else:
            if target_str[idx] in num_uppercase_dict:
                dfs(idx + 1, result_str + num_uppercase_dict[target_str[idx]])
            len_2_str = target_str[idx:idx + 2]
            if len_2_str in num_uppercase_dict and len(len_2_str) == 2:
                dfs(idx + 2, result_str + num_uppercase_dict[len_2_str])

    num_uppercase_dict = {str(num): uppercase for num, uppercase in zip(range(1, 27), string.ascii_uppercase)}
    target_str = input()

    code = []

    dfs()
    return code + [str(len(code))]

if __name__ == "__main__":
    print(solution(examine=True))
