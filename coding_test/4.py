#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'slotWheels' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY history as parameter.
#

def slotWheels(history):
    # Write your code here
    spins_count, wheels_count = len(history), len(history[0])
    # 각 spin의 숫자를 문자열로 형변환 후 오름차순으로 정렬
    history = [sorted(str(h)) for h in history]
    # 각 spin에서 n번째로 큰 숫자들 가운데 가장 큰 값을 모아놓은 리스트. 우선 '0'으로 초기화
    max_wheel = ['0'] * wheels_count
    for i in range(spins_count):
        for j in range(wheels_count):
            if history[i][j] > max_wheel[j]:
                max_wheel[j] = history[i][j]
    return sum(int(x) for x in max_wheel)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    history_count = int(input().strip())

    history = []

    for _ in range(history_count):
        history_item = input()
        history.append(history_item)

    result = slotWheels(history)

    fptr.write(str(result) + '\n')

    fptr.close()
