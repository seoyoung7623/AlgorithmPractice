# 11055 가장 큰 증가하는 부분 수열 S2
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n
dp[0] = arr[0]
for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i],dp[j]+arr[i]) #증가하는 값이여야한다.
        # else: # 이 부분이 없으면 틀리는 이유? i와 j가 같거나 j가 작은경우 갱신 
        #     dp[i] = max(dp[i],arr[i]) 
print(max(dp))