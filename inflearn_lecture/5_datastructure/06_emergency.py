
# 210718 ~ 210726
from examine import examine
from collections import deque
import sys

# 강의에서 풀어주신 방식. 이렇게 하면 그런데 속도가 너무 느림...
# 이걸 수정하기는 했는데.... 이걸 더 빠르게 바꿀 방법은 없으려나...
@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    n, m = map(int, input().split())
    Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
    Q = deque(Q)
    sorted_q = sorted(Q, key=lambda x:x[1], reverse=True)  # 추가
    cnt=0
    while True:
        cur = Q.popleft()
        if cur[1] != sorted_q[cnt][1]:  # 변경
        # if any(cur[1] < x[1] for x in Q):
            Q.append(cur)
        else:
            cnt += 1
            if cur[0] == m:
                return [[str(cnt)]]
                break

# 대충 풀기는 했는데 이렇게 하는 게 아닌 것 같다
# mysol, 이렇게 하면 testcase 4에서 문제가 생김...
# @examine
# def solution(**kwargs):
#     if kwargs['examine']:
#         sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
#     num, target = map(int, input().split())
#     patients = list(map(int, input().split()))
#     for i, p in enumerate(patients[target + 1:], start=target+1):
#         if p > patients[target]:
#             num = i
#             break
#     patients.extend(patients[:target + 1])

#     return [[str(len([t for t in patients[num:] if t >= patients[-1]]))]]

if __name__ == "__main__":
    print(solution(examine=True))
