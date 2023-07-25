# 15486 퇴사2 G5
# import sys
# input = sys.stdin.readline
# N = int(input())
# li = [list(map(int,input().split())) for _ in range(N)]
# dp = [0]*(N+1)

# for i in range(N):
#     for j in range(li[i][0]+i,N+1):
#         if dp[j]<dp[i]+li[i][1]:
#             dp[j] = dp[i]+li[i][1]
# print(dp[-1])

# 시간초과!!
# https://dndi117.tistory.com/40 참고

import sys 
input = sys.stdin.readline 
n = int(input())
t,p =[],[]
dp = [0]*(n+1)
for i in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)
M = 0
for i in range(n):
    M = max(M,dp[i])
    if i+t[i]>n:
        continue
    dp[i+t[i]] = max(M+p[i],dp[i+t[i]])
print(max(dp))