#2667 단지 번호붙이기
from collections import deque

N = int(input())

maplist = [list(map(int,input())) for _ in range(N)]
dx,dy =[-1,1,0,0],[0,0,-1,1]
queue = deque()

def bfs(x,y):
    cnt = 1
    queue.append([x,y])
    maplist[x][y] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y

            if nx<0 or nx>=N or ny<0 or ny>= N:
                continue
            if maplist[nx][ny] == 0:
                continue

            if maplist[nx][ny] == 1:
                cnt +=1
                maplist[nx][ny] = 0
                queue.append([nx,ny])
    return cnt

cntlist = []
for i in range(N):
    for j in range(N):
        if maplist[i][j] == 1:
            cntlist.append(bfs(i,j))
cntlist.sort()
print(len(cntlist))
for i in cntlist:
    print(i)