# 치즈 2636
from collections import deque


N,M = map(int,input().split()) #세로,가로

cheeze = [list(map(int,input().split())) for _ in range(N)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
cnt = 0

def bfs(x,y):
    q = deque()
    q.append([x,y])
    
    while q:
        x,y = q.popleft()
        zero = False

        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y

            if nx<0 or nx>=N or ny<0 or ny>= M:
                continue

            if cheeze[nx][ny] == 0:
                zero = True
        if zero == False:
            
                
                cheeze[x][y] = 0
                # q.append([nx,ny])

                # for j in range(4):
                #     mx,my = dx[j]+nx,dy[j]+ny

                #     if mx<0 or mx>=N or my<0 or my>= M:
                #         continue

                #     if cheeze[mx][my] == 1:
                #         q.append([mx,my])


for i in range(N):
    for j in range(M):
        if cheeze[i][j] == 1:
            bfs(i,j)
            cnt += 1
print(cnt)



