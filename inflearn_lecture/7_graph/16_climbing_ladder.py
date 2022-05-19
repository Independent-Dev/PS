from examine import examine
import sys, pprint

OFFSET_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    direction = [1, -1]
    ladder = []

    for i in range(10):
        ladder.append([int(num) for num in input().split()])
        if i == 9:
            for j in range(10):
                if ladder[-1][j] == 2:
                    target = {'y': i, 'x': j}

    while target['y']:
        for x in direction:
            next_x = x + target['x']
            if 0 <= next_x < 10 and ladder[target['y']][next_x]:
                target['x'] = next_x
                break
        else:
            target['y'] -= 1
        ladder[target['y']][target['x']] = 0

    return [str(target['x'])]

if __name__ == "__main__":
    print(solution(examine=True))
