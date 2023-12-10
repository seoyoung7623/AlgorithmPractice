# 격자상의 경로 S1
'''
내 풀이의 보완점
k를 기준으로 나눠서 곱해주면 되는데 한번에 계산하려고 한것
'''
import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())

def find(n,m):
    dp = [[0]*(m+1)]*(n+1)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m]

if k == 0:
    print(find(n,m))
else:
    dotN1 = (k-1) // m+1
    dotM1 = k - (dotN1 - 1)*m
    dotN2 = n - (dotN1-1)
    dotM2 = m - (dotM1-1)

    first = find(dotN1,dotM1)
    second = find(dotN2,dotM2)
    print(first*second)

# 내 풀이
# import sys
# input = sys.stdin.readline
# N,M,K = map(int,input().split())

# def dynamix(n,m,num):
#     dp = [[0]*m for _ in range(n)]
#     dp[0] = [num]*m
#     for i in range(1,n):
#         for j in range(m):
#             if j == 0:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#     return dp[n-1][m-1]

# if K:
#     row = K//M
#     cel = K%M
#     cnt = dynamix(row+1,cel,1)
#     print(dynamix(N-row,M-cel+1,cnt))
# else:
#     print(dynamix(N,M,1))