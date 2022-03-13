from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    stack = []
    for i in input():
        if i.isdigit():
            stack.append(i)
        else:
            back = stack.pop()
            front = stack.pop()
            stack.append(eval(f"{front} {i} {back}"))


    return [str(stack[0])]

if __name__ == "__main__":
    print(solution(examine=True))