# 2747 피보나치 수
# dp 다이나믹 프로그래밍
n = int(input())
dp = [0]*(n+1)
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n])