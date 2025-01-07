# 17142 연구소3 G3
'''
BFS
고려할점: 비활성화된 바이러스를 만나면 시간을 갱신해주지 않는다.
BFS의 큐와 visited를 이용하면 시간 순서대로 이동하기 때문에 visited =false를 기준으로 갱신하면 겹치는 부분을 고려하지 않아도 된다!
'''
from collections import deque
from itertools import combinations
import copy

N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
virus = []
INF = 1e5
answer = INF
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            grid[i][j] = '*'
            virus.append((i,j))
        elif grid[i][j] == 1:
            grid[i][j] = '-'
        else:
            grid[i][j] = -1
            
diraction = [(0,1),(1,0),(0,-1),(-1,0)]
for virus_com in list(combinations(virus,M)):
    visited = [[False]*N for _ in range(N)]
    grid_tem = copy.deepcopy(grid)
    time = 0
    q = deque(virus_com)
    for x,y in virus_com:
        grid_tem[x][y] = 0

    while q:
        x,y = q.popleft()
        visited[x][y] = True
        for dx,dy in diraction:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False and grid_tem[nx][ny] != '-':
                if grid_tem[nx][ny] == -1: # 방문하지 않은곳
                    grid_tem[nx][ny] = grid_tem[x][y] + 1
                    time = max(time,grid_tem[nx][ny]) # 방문하지 않았을때만 시간을 갱신
                elif grid_tem[nx][ny] == '*':
                    grid_tem[nx][ny] = grid_tem[x][y] + 1
                visited[nx][ny] = True
                q.append((nx,ny))
    
    for i in range(N):
        for j in range(N):
            if grid_tem[i][j] == -1:
                time = INF
    answer = min(time,answer)
if answer == INF:
    print(-1)
else:
    print(answer)





