import sys
input = sys.stdin.readline

n,k = map(int,input().split())
money = list(int(input()) for _ in range(n))
dp = [1]+[0]*k
for coin in money:
    for c in range(coin,k+1):
        dp[c] += dp[c-coin]
print(dp[k])