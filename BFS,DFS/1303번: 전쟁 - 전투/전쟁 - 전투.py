#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1303                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1303                           #+#        #+#      #+#     #
#    Solved: 2025/04/21 09:35:57 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
grid = [list(input()) for i in range(M)]
visited = [[0]*N for _ in range(M)]

diractions = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(x,y,color):
    cnt = 1
    q = deque([(x,y)])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in diractions:
            nx = x + dx
            ny = y + dy
            if 0<=nx<M and 0<=ny<N:
                if visited[nx][ny] == 0 and grid[nx][ny] == color:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return cnt**2

w_total = 0
b_total = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            if grid[i][j] == 'W':
                w_total += bfs(i,j,'W')
            elif grid[i][j] == 'B':
                b_total += bfs(i,j,'B')

print(w_total,b_total)