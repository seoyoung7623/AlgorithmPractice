'''
BFS
visited 높이차이면  +1 추가
'''
from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    INF = int(1e5)
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    
    
    def BFS(x,y):
        visited = [[INF]*N for _ in range(N)]
        q = deque([(x,y)])
        visited[x][y] = 0
        diractions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x,y = q.popleft()
            for dx,dy in diractions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < N and 0 <= ny < N:
                    diff = grid[nx][ny] - grid[x][y] if (grid[nx][ny] - grid[x][y]) > 0 else 0
                    if visited[nx][ny] > visited[x][y] + diff + 1:
                        visited[nx][ny] = visited[x][y] + diff + 1
                        q.append((nx,ny))
        return visited[N-1][N-1]
                        
    print(f"#{test_case} {BFS(0,0)}")