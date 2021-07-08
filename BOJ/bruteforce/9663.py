# 210613
# not solved yet

# my code
# target = int(input())
# count = 0

# def dfs(count, up=[], down=[], stand=[]):
#     for i in (set(range(1, target+1))-set(up)-set(down)-set(stand)):
#         if len(stand) + 1 == target:
#             return count + 1
#         count = dfs(count, [x + 1 for x in up+ [i] if x < target], [x - 1 for x in down+ [i] if 1 <= x], stand+[i])
#
#     return count
#
# print(dfs(0))

# code from other person: https://rebas.kr/761
target = int(input())
count = 0
stand, up, down = [0] * target, [0]*(2*target-1), [0]*(2*target-1)
def dfs_other(depth=0):
    global count
    if depth == target:
        count += 1
        return
    for width in range(target):
        if not (stand[width] or up[depth + width] or down[depth + target - width - 1]):
            stand[width] = up[depth + width] = down[depth + target - width - 1] = 1
            dfs_other(depth + 1)
            stand[width] = up[depth + width] = down[depth + target - width - 1] = 0

dfs_other()
print(count)
