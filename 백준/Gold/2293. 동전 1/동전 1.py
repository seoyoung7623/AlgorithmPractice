n,k = map(int,input().split())

coins = [int(input()) for _ in range(n)]
dp = [1] + ([0] * k)

for c in coins:
    for i in range(c,k+1):
        dp[i] += dp[i-c]
print(dp[k])