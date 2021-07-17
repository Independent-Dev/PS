# 210717
from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    op_dict = {
        "+": "__add__",
        "-": "__sub__",
        "*": "__mul__",
        "/": "__truediv__"
    }

    target = input()
    result = []
    for t in target:
        if t in op_dict:
            up, down = result.pop(), result.pop()
            result.append(down.__getattribute__(op_dict[t])(up))
        else:
            result.append(int(t))
    return [[str(result[0])]]

if __name__ == "__main__":
    print(solution(examine=True))
