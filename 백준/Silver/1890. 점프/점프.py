import sys
input = sys.stdin.readline
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 0:
            continue
        step = grid[i][j]
        if i+step<N:
            dp[i+step][j] += dp[i][j]
        if j+step<N:
            dp[i][j+step] += dp[i][j]

print(dp[N-1][N-1])