#1463 1로 만들기
# 동적 계획법 이용

# n = int(input())
# dp = [0,0,1,1]

# for i in range(4,n+1):
#     dp.append(dp[i-1]+1)
#     if i %2 == 0:
#         dp[i] = min(dp[i//2]+1,dp[i])
#     if i % 3 == 0:
#         dp[i] = min(dp[i//3]+1,dp[i])
# print(dp[n])

# n = int(input())
# arr = [0]*(n+1)
# for i in range(2,n+1):
#     arr[i] += arr[i-1] + 1 
#     if i%3 == 0 and arr[i//3]+1 < arr[i]:
#         arr[i] = arr[i//3] + 1
#     if i%2 == 0 and arr[i//2] +1 < arr[i]:
#         arr[i] = arr[i//2] + 1 
# print(arr[n])

#2023.07.27 dp 공부중에 다시 푸는중
n = int(input())
dp = [0]*(n+1)

for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    if i %2 == 0:
        # dp[i] = min(dp[i-1]+1,dp[i//2]+1) 
        # 2로 나누어질때 3으로 나누어질때 동시에 있을수 있기 때문에 min을 dp[i-1]와 비교하는것이 아닌 dp[i]와 비교한다.
        dp[i] = min(dp[i],dp[i//2]+1) 
    if i%3 ==0:
        dp[i] = min(dp[i],dp[i//3]+1)  
print(dp[n])