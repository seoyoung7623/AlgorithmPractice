N = int(input())
nums = list(map(int,input().split()))

dp = [[0]*21 for _ in range(N-1)]
dp[0][nums[0]] = 1

for i in range(1,N-1): #nums
    for j in range(21): #현재까지 온 수에서 num만큼 +/-
        if dp[i-1][j]:
            if 0<=j+nums[i]<=20:
                dp[i][j+nums[i]] += dp[i-1][j] # += 1
            if 0<=j-nums[i]<=20:
                dp[i][j-nums[i]] += dp[i-1][j]

print(dp[N-2][nums[-1]])
