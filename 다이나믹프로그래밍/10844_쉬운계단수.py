# 10844 쉬운 계단 수 S1
import sys
input = sys.stdin.readline
N = int(input())
dp = [[0]*10 for _ in range(N+1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N])%1000000000) 
# print(int(sum(dp[N])%1e9)) -> 소수점이 발생하면 값이 달라짐 주의