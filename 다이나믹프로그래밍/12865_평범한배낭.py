# 12865 평범항 배낭
# N,K = map(int,input().split())
# items = [list(map(int,input().split())) for _ in range(N)]
# dp = [0]*(K+1)
# for item in items:
#     for i in range(item[0],K+1):
#         if 0 <= i-item[0] <= K:
#           dp[i] = max(dp[i],dp[i-item[0]]+item[1])
        
# print(dp[-1])
        

# 탐다운 방식으로 풀기
N,K = map(int,input().split())
items = [list(map(int,input().split())) for _ in range(N)]
dp = [0]*(K+1)
for item in items:
    w,v = item
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])