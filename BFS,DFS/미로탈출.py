#미로탈출
from collections import deque

N,M = map(int,input().split())

mirro = [list(map(int,input())) for _ in range(N)]
cntList = []
queue = deque([])
dx,dy = [-1,1,0,0],[0,0,-1,1]

# def bfs(x,y):
#     if x<0 or x>=M or y<0 or y>=N:
#         return False
#     if mirro[x][y]==1:
#         cnt += 1
#         mirro[x][y] = 0

def bfs():
    cnt = 0
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = dx[i] + x,dy[i]+y

            if 0 <= nx < M and 0 <= ny < N and mirro[nx][ny] == 0:
                cnt +=1
                queue.append([nx,ny])
            
            if nx == M-1 and ny == N-1:
                break
    cntList.append(cnt)


# for i in range(N):
#     for j in range(M):
#         bfs(i,j)

for i in range(N):
    for j in range(M):
        if mirro[i][j] == 1:
            queue.append([i,j])
bfs()

print(min(cntList))
