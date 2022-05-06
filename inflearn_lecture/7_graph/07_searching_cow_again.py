from examine import examine
import sys, string

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    current_pos, target_pos = [int(num) for num in input().split()]

    visited = [0] * (target_pos + abs(target_pos - current_pos))
    pos_list = [current_pos]
    count = 0

    while not visited[target_pos]:
        temp_pos = []
        for pos in pos_list:
            for offset in [-1, 1, 5]:
                next_pos = pos + offset
                if 0 < next_pos < len(visited) and not visited[next_pos]:
                    visited[next_pos] = 1
                    temp_pos.append(next_pos)
        pos_list = temp_pos
        count += 1

    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=True))
