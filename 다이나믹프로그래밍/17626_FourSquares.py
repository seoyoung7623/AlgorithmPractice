# 17626 Four Squares
# 1. dp pypy3로 제출
import sys
import math
input = sys.stdin.readline
n = int(input())
dp = [0,1]

for i in range(2, n+1):
    minValue = 1e9
    for j in range(1, int(math.sqrt(i))+1):
        minValue = min(minValue,dp[i-j**2])
    dp.append(minValue + 1)

print(dp[n])

# 2. 부루트포스
# import math
# def fourSquares(n):
#     if int(math.sqrt(n)) == math.sqrt(n):
#         return 1
#     for i in range(1,int(math.sqrt(n))+1):
#         if int(math.sqrt(n-i**2)) == math.sqrt(n-i**2):
#             return 2
#     for i in range(1,int(math.sqrt(n))+1):
#         for j in range(1,int(math.sqrt(n-i**2)+1)):
#             if int(math.sqrt(n-i**2-j**2)) == math.sqrt(n-i**2-j**2):
#                 return 3
#     return 4 


# n = int(input())
# print(fourSquares(n))
