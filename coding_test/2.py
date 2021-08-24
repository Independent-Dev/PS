#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getMin(s):
    # Write your code here
    left, right = 0, 0  # 각각 balanced 되지 않은 괄호의 개수
    for p in s:
        if p == "(":
            left += 1
        else:
            if left != 0:
                left -= 1
            else:
                right += 1
    return left + right
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getMin(s)

    fptr.write(str(result) + '\n')

    fptr.close()
