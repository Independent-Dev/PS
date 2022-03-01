import sys, math
from examine.examine import examine



@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    applicant_list = []

    N = int(input())
    for _ in range(N):
        applicant_list.append([int(x) for x in input().split()])

    applicant_list.sort(key=lambda x:-x[0])

    count = 1
    prev_kg = applicant_list.pop(0)[1]

    for applicant in applicant_list:
        if applicant[1] > prev_kg:
            count += 1
            prev_kg = applicant[1]

    return [str(count)]

if __name__ == "__main__":
    print(solution(examine=True))