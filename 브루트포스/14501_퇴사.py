# 14501 퇴사 
'''
브루트포스, DP
'''
n = int(input())
dp = [0] * (n+1) # 총 가격을 구해야하기때문에 하루 추가!
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+arr[i][0],n+1):
        dp[j] = max(dp[j],dp[i]+arr[i][1])
print(dp[-1])

