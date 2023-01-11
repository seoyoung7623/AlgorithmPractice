#14502 연구소
from collections import deque
import copy
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
maplist = [list(map(int,input().split())) for _ in range(n)]
ans = 0
dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs():
    tmp_graph = copy.deepcopy(maplist)
    q = deque()
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i] + x,dy[i]+y
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append((nx,ny))
    global ans
    sum = 0
    for i in range(n):
        sum += tmp_graph[i].count(0)
    ans = max(ans,sum)

def makeWall(cnt): #카운트 벽 3개를 만들고 BFS를 진행해야하므로 재귀함수이용!
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if maplist[i][j] == 0:
                maplist[i][j] = 1
                makeWall(cnt+1) #재귀함수!!
                maplist[i][j] = 0 #다 돌리고 돌아오면 0으로 바꿔줌

makeWall(0)
print(ans)

#튜플() , deepcopy