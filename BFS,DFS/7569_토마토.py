# 7569 토마토
from collections import deque
import sys
imput = sys.stdin.readline


M,N,H = map(int,input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

cnt = 0
queue = deque()
visited = list(list([0]*M for _ in range(N)) for _ in range(H))

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def BFS():
    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H and visited[nz][ny][nx] == 0 and box[nz][ny][nx] == 0:
                visited[nz][ny][nx] = 1
                queue.append([nz,ny,nx])
                box[nz][ny][nx] = box[z][y][x] +1 #마지막에 회수를 계산하기 위해 전에 값에 1을 더해줌.


for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1 and visited[i][j][k] == 0:
                queue.append([i,j,k]) #한번에 1이 있는 곳부터 탐색해야하니까 일단 추가해준다.
                visited[i][j][k] = 1
                
                
BFS()

for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0) 
        cnt = max(cnt,max(j))
print(cnt-1)