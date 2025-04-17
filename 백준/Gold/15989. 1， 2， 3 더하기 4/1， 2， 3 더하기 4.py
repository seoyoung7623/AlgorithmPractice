T = int(input())
dp = [1]*10001 # 1로만 만드는 수는 1개씩 존재함

for i in range(2,10001):
    dp[i] += dp[i-2]

for i in range(3,10001):
    dp[i] += dp[i-3]

for test_case in range(T):
    answer = int(input())
    print(dp[answer])