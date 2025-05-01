import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split()) # 세로, 가로
board = [list(input()) for _ in range(N)]
walls = set()
coins = []

diractions = [(1,0),(0,1),(-1,0),(0,-1)]

def is_inside(x,y):
    return 0<=x<N and 0<=y<M

def bfs():
    q = deque()
    x1,y1 = coins[0]
    x2,y2 = coins[1]
    visited = set()
    q.append((x1,y1,x2,y2,0))
    visited.add((x1,y1,x2,y2))
    while q:
        x1,y1,x2,y2,cnt = q.popleft()
        if cnt >= 10:
            return -1
        for dx,dy in diractions:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy

            fall1 = not is_inside(nx1,ny1)
            fall2 = not is_inside(nx2,ny2)

            if fall1 and fall2:
                continue
            if fall1 or fall2:
                return cnt + 1
            
            # 벽이면 이동할 수 없음
            if board[nx1][ny1] == '#':
                nx1,ny1 = x1, y1
            if board[nx2][ny2] == '#':
                nx2,ny2 = x2, y2
            
            if (nx1,ny1,nx2,ny2) not in visited:
                visited.add((nx1,ny1,nx2,ny2))
                q.append((nx1,ny1,nx2,ny2,cnt+1))
    return -1
            
            
# 동전 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i,j))
            board[i][j] = '.'
            
        
print(bfs())