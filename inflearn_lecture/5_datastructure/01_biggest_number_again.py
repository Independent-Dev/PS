from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    target, count = input().split()
    stack = []
    count = int(count)
    for i, t in enumerate(target):
        while stack and stack[-1] < t:
            stack.pop()
            count -= 1
            if not count:
                return [''.join(stack) + target[i:]]
        stack.append(t)

    return [''.join(stack[:-count])]

if __name__ == "__main__":
    print(solution(examine=True))