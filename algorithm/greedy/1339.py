# 210621 단어 수학 gold4
# greedy / bruteforce
import sys
from collections import defaultdict
def input_processing():
    word = input().strip()
    for i, w in enumerate(word, start=1):
        word_dict[w] += 10 ** (len(word) - i)

input = sys.stdin.readline
word_dict = defaultdict(int)
result, start = 0, 9

N = int(input())
for _ in range(N):
    input_processing()

for v in sorted(word_dict.values(), reverse=True):
    result += v * start
    start -= 1

print(result)


