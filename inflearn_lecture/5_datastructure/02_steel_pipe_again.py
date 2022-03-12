from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    pipe = input()
    res = pipe_count = 0
    for i, p in enumerate(pipe):
        if p == "(":
            pipe_count += 1
        else:
            pipe_count -= 1
            if pipe[i - 1] == "(":
                res += pipe_count
            else:
                res += 1
    return [str(res)]

if __name__ == "__main__":
    print(solution(examine=True))