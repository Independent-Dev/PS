import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    answer = ''
    for i in input():
        if i.isdigit():
            answer += i

    num = int(answer)
    aliquot_count = 0  # 약수의 개수

    for n in range(1, num + 1):
        if num % n == 0:
            aliquot_count += 1
    return [str(num), str(aliquot_count)]

if __name__ == "__main__":
    print(solution(examine=True))