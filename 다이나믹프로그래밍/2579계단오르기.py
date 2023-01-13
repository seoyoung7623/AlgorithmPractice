#2579 계단 오르기
'''
n = int(input())
numlist = []
conlist = []
for _ in range(n):
    sta = int(input())
    numlist.append(sta)
i = 0
total = 0
while i <= n:
    if (i+1) >= n or (i+2) >= n:
        print(total)
        break
    sum1 = numlist[i] + numlist[i+1]
    sum2 = numlist[i] + numlist[i+2]
    if sum1>sum2
'''
"""
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1]+s[2],s[0],s[2])
for i in range(3,n):
     dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i]) #앞: 마지막계단의 전계단를 밟은 경우 무조건 전전은 2칸 / 뒤: 마지막계단의 전 계단을 밟지 않은 경우
print(dp[n-1])
"""
n = int(input())
s = [0 for _ in range(301)]
dp =[0 for _ in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[1] + s[0]
dp[2] = max(s[0]+s[2],s[1]+s[2])
for i in range(3,n):
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2]+ s[i])
print(dp[n-1])

