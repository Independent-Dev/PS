# 210613
# not solved yet

# my code
# a, b, c = [int(num) for num in input().split()]
#
# print(c - ((abs(a - c) ** b) % c))

# others code: https://jjangsungwon.tistory.com/10
A, B, C = [int(num) for num in input().split()]

def devide_and_conquer(A, B):
    if B == 1:
        return A % C
    result = devide_and_conquer(A, B // 2)
    if B % 2 == 0:
        return result * result % C
    else:
        return result * result * A % C

print(devide_and_conquer(A, B))
