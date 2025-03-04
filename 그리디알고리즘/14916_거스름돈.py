# S5
'''
거스름돈: 5원,2원
홀수면 5를 홀수개로 나눔
짝수면 5를 짝수개로 나눔
'''
# 1. 그리디 풀이법
n = int(input())
answer = 0
answer += n//5
if (n%5)%2 != 0:
    if answer >= 1:
        answer -= 1
        answer += (n % 5 + 5 )//2
        print(answer)
    else:
        print(-1)
else:
    answer += (n%5)//2
    print(answer)
        
# 2. DP 풀이방식
# 거르름돈 경우의수가 많은 때 고려하기
n = int(input())
answer = 0
dp = [-1] * (n+1)
if n >= 2:
    dp[2] = 1
if n >= 4:
    dp[4] = 2
if n >=5:
    dp[5] = 1

for i in range(6,n+1):
    if dp[i-2] != -1:
        dp[i] = dp[i-2] + 1
    if dp[i-5] != -1:
        dp[i] = min(dp[i-5] + 1,dp[i])
print(dp[n])
    
    
    
