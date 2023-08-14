# 14940 쉬운최단 거리 S1
from collections import deque


n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = list([0]*m for _ in range(n))
result = list([0]*m for _ in range(n))
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def BFS(result,x,y): # 초기 위치
    queue = deque()
    visited[x][y] = 1
    queue.append([x,y])
    
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    continue
                result[nx][ny] = result[x][y] + 1
                queue.append([nx,ny])

# 목표지점을 찾음
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            BFS(result,i,j)
            break
        else:
            continue

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 1:
            result[i][j] = -1

for i in range(n):
    print(*result[i])

