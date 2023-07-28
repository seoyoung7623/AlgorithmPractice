# 11726 2Xn 타일링
# dp 다이나믹 프로그래밍

n = int(input())
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)
