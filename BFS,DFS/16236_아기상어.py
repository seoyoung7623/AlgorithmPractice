# 16236 아기상어 G3
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result= 0

def BFS(x,y,size,eat):
    global result
    q = deque()
    q.append((x,y))
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    while q:
        x,y = q.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if size<graph[nx][ny]:
                    continue
                if graph[nx][ny] !=0 and graph[nx][ny]<size:
                    eat += 1
                visited[nx][ny] = min(visited[x][y] + 1,visited[nx][ny])
                q.append((nx,ny))
                if eat == graph[nx][ny]:
                    result += visited[nx][ny]
                    visited = [[0]*N for _ in range(N)]
                    eat = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            BFS(i,j,2,0)

print(result)