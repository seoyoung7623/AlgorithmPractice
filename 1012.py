#1012 유기농배추
from collections import deque

def bfs(graph,a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue: ## queue를 다 탐색할때까지 반복하는것 같은데 queue가 하나밖에 없는거 아님? = while q: 큐가 빌때까지 반복실행
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or nx >= n or ny <0 or ny>= m:
                continue
            if graph[nx][ny] == 1: #주변에 1이 있나 확인
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return


dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

for i in range(t):
    cnt = 0
    n,m,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x,y = map(int,input().split())
        graph[x][y] = 1
    
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph,a,b)
                cnt +=1
    print(cnt)