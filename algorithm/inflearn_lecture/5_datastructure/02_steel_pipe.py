# 210703
# 문제 분석에서 살짝 실수가 있었구만...
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    input_str = input()
    pipe_count, result = 0, 0
    for i, s in enumerate(input_str[1:], start=1):
        if s == "(":
            pipe_count += 1
        else:
            if input_str[i-1] == "(":  # 이 if문의 point를 처음에 잘 잡지 못했음...
                result += pipe_count
            else:
                result += 1
            pipe_count -= 1

    return [[str(result)]]

if __name__ == "__main__":
    print(solution(examine=True))

# #### 문제 분석
# * 입력
#   * 괄호
#   * 해석
# * 출력쌍
#   * 잘린 쇠막대의 수
# * 조건
#
# #### 설계
# * 필요 변수
#   * inp #
#   * pipe_count = -1 # 파이프의 개수
#   * result = 0 # 나뉜 전체 파이프의 수
# * 로직
#   * "("가 나오면 pipe_count += 1
#   * ")"가 나오면 result += pipe_count; pipe_count -= 1;
# * 필요 시간
#   * O(n)