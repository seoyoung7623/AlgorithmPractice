
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    n = N//10
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 3
    
    for i in range(3,n+1):
        dp[i] = (dp[i-2])*2+ (dp[i-1])
    print(f"#{test_case} {dp[n]}")