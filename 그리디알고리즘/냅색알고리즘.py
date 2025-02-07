# 냅색 알고리즘 py

# 1. 2차원 리스트 풀이

n,k = map(int,input().split()) # 물건의 개수 무개
wv_lst = [list(map(int,input().split())) for _ in range(n)] #무게 와 가치
wv_lst.insert(0,[0,0])

def knapsack_optimized():
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1,n+1):
        weight = wv_lst[i][0]
        value = wv_lst[i][1]
        for j in range(1,k+1):
            if j < weight: # 현재 무개가 작을 때
                dp[i][j] = dp[i-1][j]
            else: #현재 무게가 작거나 같을 때 갱신
                dp[i][j] = max(dp[i-1][j],dp[i][j-weight]+value)
    return dp[n][k]

# 2. 1차원 리스트 풀이 뒤에서 부터 갱신
def knapsack_optimized_2():
    dp = [0] * (k+1)
    for w,v in wv_lst:
        for i in range(k,w-1,-1):
            dp[i] = max(dp[i],dp[i-w]+v)
    return dp[k]
        
print(knapsack_optimized())
