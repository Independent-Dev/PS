target_str, num, divisor_count = input(), '', 2

for t in target_str:
    if t.isdigit():
        num += t

num = int(num)
for i in range(2, num):
    if num % i == 0:
        divisor_count += 1

print(num)
print(divisor_count)