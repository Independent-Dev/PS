# 210703
# 문제 분석에서 살짝 실수가 있었구만...
# 살짝 수준이 아니었던 것으로 드러났음... 힘들었다... 앞으로는 문제 푸는 데 걸리는 시간도 체크해야겠다...
from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    input_str = input()
    result, _ = infix_to_postfix(0)
    return [[result]]

def infix_to_postfix(i):
    result = ''
    num_list, pre_op_list, post_op_list = [], [], []
    while i < len(input_str):
        if input_str[i] == "(":
            temp_result, i = infix_to_postfix(i+1)
            result += temp_result
        elif input_str[i] == ")":
            break
        else:
            if input_str[i] in "*/":
                if pre_op_list:
                    result += pre_op_list.pop()
                pre_op_list.append(input_str[i])
            elif input_str[i] in "+-":
                while pre_op_list:
                    result += pre_op_list.pop()
                if post_op_list:
                    result += post_op_list.pop()
                post_op_list.append(input_str[i])
            else:
                result += input_str[i]
            i += 1
    while pre_op_list:
        result += pre_op_list.pop()
    while post_op_list:
        result += post_op_list.pop()
    return result, i + 1


if __name__ == "__main__":
    print(solution(examine=True))

# #### 문제 분석
# * 입력
#   * 중위표현식
#   * 해석
# * 출력쌍
#   * 후위표현식
# * 조건
#
# #### 설계
# * 필요 변수
# * 로직
#   * 숫자는 순서, 연산자는 우선 순위 순서대로...
#   * 처음에 해석 함수 호출
#   * "("가 오면
# * 필요 시간