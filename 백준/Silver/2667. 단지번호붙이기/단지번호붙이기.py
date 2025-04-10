from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

diractions = [(1,0),(0,1),(0,-1),(-1,0)]

def BFS(x,y,number):
    q = deque([(x,y)])
    visited[x][y] = number
    cnt = 1
    while q:
        sx,sy = q.popleft()
        for dx,dy in diractions:
            nx = sx + dx
            ny = sy + dy
            if 0<=nx<N and 0<=ny<N:
                if grid[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = number
                    cnt += 1
                    q.append((nx,ny))
    return cnt

number = 0
arr = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and visited[i][j] == 0:
            number += 1
            arr.append(BFS(i,j,number))
print(len(arr))
arr.sort()
for a in arr:
    print(a)