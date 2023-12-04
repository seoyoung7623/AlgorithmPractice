# 2231 분해합 B2
n = int(input())
result = 0
for i in range(n):
    num = sum(map(int,str(i)))
    num_sum = num + i
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)
    