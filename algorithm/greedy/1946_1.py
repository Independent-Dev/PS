# 210606
import sys

def make_array():
    length = int(sys.stdin.readline().strip())
    array = [0] * (length + 1)

    # 우선 첫 시험 결과로 두 번째 시험의 결과를 정렬하여 저장
    for _ in range(length):
        first, second = list(map(int, sys.stdin.readline().strip().split()))
        array[first] = second

    return array[1:]


def max_qualifier(result):
    MAX = 100001
    count = 0

    for second in result:
        # 첫 번째 시험 결과가 앞 사람보다 좋지 않지만, 두 번째 시험 결과는 더 나은 경우
        if second < MAX:
            count += 1
            MAX = second
    return count


test_count = int(sys.stdin.readline().strip())
test_result = []

for _ in range(test_count):
    test_result.append(make_array())

for result in test_result:
    print(max_qualifier(result))