from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    session_order = input()
    res = []
    for i in range(int(input())):
        target = input()
        idx = 0
        for s in target:
            if s == session_order[idx]:
                idx += 1
                if idx == len(session_order):
                    break
            elif s in session_order:
                break

        if idx == len(session_order):
            res.append(f"#{i + 1} YES")
        else:
            res.append(f"#{i + 1} NO")

    return res

if __name__ == "__main__":
    print(solution(examine=True))