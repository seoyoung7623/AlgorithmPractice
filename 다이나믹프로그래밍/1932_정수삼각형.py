# 1932 정수 삼각형
# DP
n = int(input())
tree = [[]]
for _ in range(n):
    tree.append(list(map(int,input().split())))
dp = [list([0]* i) for i in range(0,n+1)]
dp[1][0]=tree[1][0]
for i in range(2,n+1):
    for j in range(i):
        if j == 0:
            dp[i][j] = tree[i][j] + dp[i-1][j]
        elif j == i-1:
            dp[i][j] = tree[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = tree[i][j] + max(dp[i-1][j],dp[i-1][j-1])

result = max(int(dp[n][i]) for i in range(n))
print(result)
