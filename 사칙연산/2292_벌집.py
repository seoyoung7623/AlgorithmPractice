# 2292 벌집 B2
N = int(input())
n = N-1
i = 0
if n == 0:
    print(1)
else:
    while n>0:
        n = n-(6*i)
        i += 1
    print(i)