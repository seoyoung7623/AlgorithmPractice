N = int(input())

power = list(map(int,input().split()))
happy = list(map(int,input().split()))

answer = 0

dp = [0] * 101

for i in range(N):
    for p in range(100,power[i]-1,-1):
        dp[p] = max(dp[p], happy[i] + dp[p-power[i]])

print(dp[99])