import sys
from examine.examine import examine

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    prime_number_list = [2]
    if N != 2:
        for i in range(3, N + 1):
            for prime in prime_number_list:
                if i % prime == 0:
                    break
            else:
                prime_number_list.append(i)

    return [str(len(prime_number_list))]

if __name__ == "__main__":
    print(solution(examine=True))