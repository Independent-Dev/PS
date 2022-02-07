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

    # 나름 최적화하면 이런 식의 코드도 가능하긴 함.
    # for n in range(1, int(num ** 0.5) + 1):
    #     if num % n == 0:
    #         aliquot_count += 2

    # if num % n == 0 and float(n) == num ** 0.5:
    #     aliquot_count -= 1

    for n in range(1, num + 1):
        if num % n == 0:
            aliquot_count += 1
    return [str(num), str(aliquot_count)]

if __name__ == "__main__":
    print(solution(examine=True))