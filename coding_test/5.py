#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getUsernames' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER threshold as parameter.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>
#

import json, urllib.request

url = 'https://jsonmock.hackerrank.com/api/article_users?page='


def getData(page, threshold):
    res_str = urllib.request.urlopen(url + str(page)).read().decode('utf-8')
    res_dict = json.loads(res_str)
    result = []
    for data in res_dict['data']:
        if data['submission_count'] > threshold:
            result.append(data['username'])
    return result, res_dict['total_pages']


def getUsernames(threshold):
    # Write your code here
    result, total_pages = getData(1, threshold)
    for i in range(2, total_pages + 1):
        temp_result, _ = getData(i, threshold)
        result.extend(temp_result)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    threshold = int(input().strip())

    result = getUsernames(threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
