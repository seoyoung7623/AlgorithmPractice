#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2738                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2738                           #+#        #+#      #+#     #
#    Solved: 2025/04/21 11:39:08 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
grid1 = [list(map(int,input().split())) for _ in range(N)]
grid2 = [list(map(int,input().split())) for _ in range(N)]
answer = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        answer[i][j] = grid1[i][j] + grid2[i][j]

for i in range(N):
    print(*answer[i])
