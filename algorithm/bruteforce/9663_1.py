# 210616

def n_queen(depth):
    if depth == n:
        global result
        result += 1
        return
    for w in range(n):
        if not (width[w] or up[w + depth] or down[w - depth]):
            width[w] = up[w + depth] = down[w - depth] = 1
            n_queen(depth + 1)
            width[w] = up[w + depth] = down[w - depth] = 0

n = int(input())
result = 0
width, up, down = [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1)
n_queen(0)
print(result)