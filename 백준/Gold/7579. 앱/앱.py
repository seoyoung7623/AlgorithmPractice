N,M = map(int,input().split())

mem = list(map(int,input().split()))
cost = list(map(int,input().split()))
max_c = sum(cost)

dp = [0] * (max_c+1)

for i in range(N):
    for j in range(max_c,cost[i]-1,-1):
        dp[j] = max(dp[j], dp[j-cost[i]] + mem[i])

for i in range(max_c+1):
    if dp[i] >= M:
        print(i)
        break