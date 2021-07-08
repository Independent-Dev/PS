# 210703
# 어렵지 않게 풀 거라고 생각했는데 생각보다 좀 헤매었
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    target, count = input().split()
    result, count = [target[0]], int(count)
    for i, t in enumerate(target[1:], start=1):
        while result and t > result[-1]:
            result.pop()
            count -= 1
            if count == 0:
                result.extend(target[i:])
                return [[''.join(result)]]
        else:
            result.append(t)

    return [[''.join(result[:-count])]]

if __name__ == "__main__":
    print(solution(examine=True))