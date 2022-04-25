# silver3
# 220425

def solution():
    x1, y1, x2, y2 = [int(num) for num in input().strip().split()]
    count = 0

    for _ in range(int(input())):
        x3, y3, r = [int(num) for num in input().strip().split()]
        len_1 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** (1/2)
        len_2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1/2)

        if len_1 > r > len_2 or len_2 > r > len_1:
            count += 1
    print(count)

for _ in range(int(input())):
    solution()

