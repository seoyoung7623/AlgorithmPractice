#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1890                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1890                           #+#        #+#      #+#     #
#    Solved: 2025/04/18 09:28:15 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
경로의 개수
'''
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