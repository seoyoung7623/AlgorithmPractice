# 치즈 2636
""" from collections import deque


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



import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [] 
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []

def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    cnt = 0
    # 한번 while문 끝날 때마다 1시간 지난다.
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0: #검사를 안한 경우라면
                if graph[nx][ny] == 0: #치즈가 없는 부위
                    visited[nx][ny] = 1
                    # 치즈가 아닌 부분만 q에 넣어준다.
                    # 가장자리만 체크해주기위함
                    q.append([nx,ny]) #치즈가 없는 부위만 들어감
                elif graph[nx][ny] == 1: #치즈가 있는 부위
                    # !!!!!!!!!!!!!!!!!!!!!!!!이부분이 중요!!!!!!!!!!!!!!!!!!!!!!!!!!

                    # 가장자리 부분만 처리해주기때문에 만약에 공기와 접촉한 칸은 q에 넣어주지않는다.
                    # 넣게되면 안쪽 치즈까지 녹음 처리 되기 때문이다.
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt

time = 0
while 1:
    time +=1
    # 특수한 경우이기 때문에 0,1 밖에 없긴하지만 visited 리스트를 하나 만들어준다.
    # 0을 1로 바꾸거나 1을 0으로 바꾸면 방문처리가 되지만, 그렇게되면 bfs특성상 다르게 구현이된다.
    visited = [[0]*m for _ in range(n)]
    cnt = bfs() 
    if cnt == 0:
        break
print(time-1) #총시간
print(ans[-2]) # 녹기 한 시간 전 남아있는 치즈 조각
"""
## 0인경우는 queue에 넣고 1인경우를 0으로 바꿔준다.

#################################################
from collections import deque
import sys
# input = sys.stdin.readline

n,m = map(int,input().split())
cheeze = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
ans = []

def bfs():
    cnt = 0
    q = deque()
    q.append([0,0])
    visited[0][0] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+ x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if cheeze[nx][ny] == 0: #치즈가 없는 부위
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                elif cheeze[nx][ny] == 1: #치즈부위라면
                    visited[nx][ny] = 1
                    cheeze[nx][ny] = 0
                    cnt += 1
    ans.append(cnt)
    return cnt

time = 0
while 1:
    time += 1
    visited = [[0]*m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break
print(time - 1)
print(ans[-2])
