# 게임맵 최단거리 Lv2
from collections import deque

def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    q = deque([(0,0)])
    width = len(maps[0])
    height = len(maps)
    visited = list([0]*width for _ in range(height))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0>nx or nx>= height or 0>ny or ny>= width or maps[nx][ny] == 0 or visited[nx][ny] != 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))
    return visited[height-1][width-1] if visited[height-1][width-1] else -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))