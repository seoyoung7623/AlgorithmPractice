N = int(input())
# dp = list([0]*3 for _ in range(N))
# dp[0][0],dp[0][1],dp[0][2] = 1,1,1
dp = [1]*3

for i in range(1,N):
    next_dp = [0]*3
    next_dp[0] = dp[0] + dp[1] + dp[2]
    next_dp[1] = dp[0] + dp[2]
    next_dp[2] = dp[0] + dp[1]
    dp = next_dp
print(sum(dp)%9901)