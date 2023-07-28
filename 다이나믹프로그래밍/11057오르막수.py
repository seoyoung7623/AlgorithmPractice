# 11057 오르막 수
# 실버1
N = int(input())
dp = list([0]*10 for _ in range(N+1))
ans = 0

dp[1] = list([1]*10)
for i in range(2,N+1):
    for j in range(0,10):
        dp[i][j] = sum(dp[i-1][j:])

for i in range(10):
    ans += dp[N][i]
print(ans%10007)
