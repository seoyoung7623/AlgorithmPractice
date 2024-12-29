# 16234 인구이동 G4
'''
값 갱신 -> 좌표를 저장해서 갱신
완전탐색 BFS
'''
from collections import deque

N,L,R = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()

def BFS(x,y,sum):
    q.append((x,y))
    visited[x][y] = 1
    union = [(x,y)]
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < N and 0<= ny < N and visited[nx][ny] == 0:
                if L<=abs(grid[nx][ny] - grid[x][y])<=R:
                    visited[nx][ny] = 1
                    sum += grid[nx][ny]
                    union.append((nx,ny))
                    q.append((nx,ny))
    if len(union) == 1:
        return 0
    else:
        result = sum//len(union)
        for x,y in union:
            grid[x][y] = result
        return 1
day = 0
while 1:
    visited = [[0]*N for _ in range(N)]
    stop = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                stop += BFS(i,j,grid[i][j])
    if stop == 0:
        break
    day += 1
print(day)

