# 10026 적록색약 G5
from collections import deque


N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0]*(N) for _ in range(N)]
visited_RG = [[0]*(N) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()

def BFS(x,y,visited):
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<= ny <N and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))


# 적록색약이 아닌경우
cnt1 = 0
for i in range(N): #그래프 구역을 구하는 문제: 그래프를 돌면서 방문안한곳에서 BFS를 진행한다.
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j,visited)
            cnt1 += 1

#적록색약인 경우
cnt2 = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited_RG[i][j]:
            BFS(i,j,visited_RG)
            cnt2 += 1

print(cnt1, cnt2)
