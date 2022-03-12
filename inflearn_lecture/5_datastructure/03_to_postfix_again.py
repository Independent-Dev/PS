from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    def to_postfix(i=0, res=''):
        stack = []

        while i < len(target):
            current_str = target[i]
            if current_str.isdigit():
                res += current_str
            elif current_str == '(':
                i, res = to_postfix(i + 1, res)
            elif current_str == ')':
                break
            else:
                if stack and stack[-1] in ['*', '/']:
                    res += stack.pop()
                if stack and current_str in ['+', '-']:
                    res += stack.pop()
                stack.append(current_str)
            i += 1

        while stack:
            res += stack.pop()

        return i, res

    target = input()
    _, res = to_postfix()

    return [res]

if __name__ == "__main__":
    print(solution(examine=True))