# 9095 1,2,3더하기 S2
import sys
input = sys.stdin.readline
T = int(input())
dp = [0]*12
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
for t in range(T):
    N = int(input())
    print(dp[N])
