N = int(input())
list = list(map(int,input().split()))
dp = [0]*(N+1)
dp[1] = list[0]

for i in range(1,N+1):
    for j in range(1,i):
        dp[i] = max(dp[i-j]+dp[j],list[i-1],dp[i])
print(max(dp))