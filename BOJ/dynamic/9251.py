# 211007 LCS 
# gold 5
str_1 = input()
str_2 = input()

lcs_vector = [[0] * (len(str_2) + 1) for _ in range((len(str_1) + 1))]

for i, s_1 in enumerate(str_1, start=1):
    for j, s_2 in enumerate(str_2, start=1):
        if s_1 == s_2:
            lcs_vector[i][j] = lcs_vector[i-1][j-1] + 1
        else:
            lcs_vector[i][j] = max(lcs_vector[i][j-1], lcs_vector[i-1][j])
print(lcs_vector[-1][-1])
