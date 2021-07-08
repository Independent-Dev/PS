import sys

def make_array():
    array = [0] * int(input())
    for i, val in enumerate([int(x) for x in sys.stdin.readline().split()]):
        array[i] = val

    return array

def max_benefit(arr):
    M, result = arr[-1], 0
    for a in arr[-2::-1]:
        if a <= M:
            result += M - a
        else:
            M = a

    return result

test_count = int(input())
test_inp = []

for _ in range(test_count):
    test_inp.append(make_array())

for arr in test_inp:
    print(max_benefit(arr))
