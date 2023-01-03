#2178 미로탐색

from collections import deque


N,M = map(int,input().split())

mirro = [list(map(int,input())) for _ in range(N)]
dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs(x,y):
    queue = deque([])
    queue.append([x,y])

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
        
            if nx<0 or nx>= N or ny<0 or ny>= M:
                continue
            if mirro[nx][ny] == 0:
                continue

            if mirro[nx][ny] == 1:
                mirro[nx][ny] = mirro[x][y] + 1
                queue.append([nx,ny])
    return mirro[N-1][M-1]
            
print(bfs(0,0))


    
