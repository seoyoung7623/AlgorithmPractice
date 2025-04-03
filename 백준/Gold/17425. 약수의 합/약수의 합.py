import sys
input = sys.stdin.readline
T = int(input())
MAX = 1000000
g = [0] * (MAX + 1)
f = [0] * (MAX + 1)

# 약수의 합: 배수값에 해당값을 더함
for i in range(1, MAX + 1):
    for j in range(i,MAX + 1,i):
        g[j] += i
    f[i] = f[i-1] + g[i]

ans = []
for test_case in range(T):
    N = int(input())
    ans.append(N)
for i in ans:
    print(f[i])