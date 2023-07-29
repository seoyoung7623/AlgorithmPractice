# 11057 오르막 수
# 실버1
# N = int(input())
# dp = list([0]*10 for _ in range(N+1))
# ans = 0

# dp[1] = list([1]*10)
# for i in range(2,N+1):
#     for j in range(0,10):
#         dp[i][j] = sum(dp[i-1][j:])

# for i in range(10):
#     ans += dp[N][i]
# # 그냥 ans = sum(dp[N]) 해도됨 sum 은 리스트안에 있는 모든 값을 더하는 함수
# print(ans%10007)


# 앞쪽에 숫자를 추가하는 경우
N = int(input())
dp = [1]*10
for _ in range(N):
    for j in range(1,10):
        dp[j] +=dp[j-1]
print(dp[-1]%10007)
