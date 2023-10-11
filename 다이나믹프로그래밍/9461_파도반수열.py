# 9461 파도반 수열 S3
T = int(input())

dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1
for _ in range(T):
    N = int(input())
    for i in range(3,N):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[N-1])
