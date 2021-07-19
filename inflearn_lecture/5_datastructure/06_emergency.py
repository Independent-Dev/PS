# 210718
# 대충 풀기는 했는데 이렇게 하는 게 아닌 것 같다

# mysol, 이렇게 하면 testcase 4에서 문제가 생김...
from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    num, target = map(int, input().split())
    patients = list(map(int, input().split()))
    for i, p in enumerate(patients[target + 1:], start=target+1):
        if p > patients[target]:
            num = i
            break
    patients.extend(patients[:target + 1])

    return [[str(len([t for t in patients[num:] if t >= patients[-1]]))]]

if __name__ == "__main__":
    print(solution(examine=True))
