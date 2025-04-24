#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1743                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1743                           #+#        #+#      #+#     #
#    Solved: 2025/04/23 09:46:30 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split()) #세로,가로,개수
grid = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = 0
for _ in range(K):
    x,y = map(int,input().split())
    grid[x-1][y-1] = 1

diractions = [(1,0),(0,1),(-1,0),(0,-1)]
def BFS(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        for dx,dy in diractions:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M:
                if grid[nx][ny] == 1 and visited[nx][ny] == 0:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return cnt

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            answer = max(answer,BFS(i,j))
            
print(answer)