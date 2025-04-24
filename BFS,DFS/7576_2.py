#7576 토마토
from collections import deque

M,N = map(int,input().split()) #M 가로 N 세로

tomato = [list(map(int,input().split())) for _ in range(N)]
queue = deque([])
dx,dy = [-1,1,0,0],[0,0,-1,1]


def bfs():
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
    
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if tomato[nx][ny] == 0: ##이부분 != -1로 했었음ㅜㅜ
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx,ny])






for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i,j])

bfs()
res=0

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res,max(i))
print(res-1)
