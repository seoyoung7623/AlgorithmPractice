n,k = map(int,input().split())
INF = int(1e6)
dp = [INF]*(k+1)
dp[0] = 0 # 0원은 0개!
coins = [int(input()) for _ in range(n)]

for coin in coins:
    for i in range(coin,k+1):
        dp[i] = min(dp[i],dp[i-coin]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])