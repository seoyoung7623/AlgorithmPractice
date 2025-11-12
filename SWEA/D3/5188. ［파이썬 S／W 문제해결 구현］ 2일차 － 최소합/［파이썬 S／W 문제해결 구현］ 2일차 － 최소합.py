from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    INF = int(1e4)
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    visited = [[INF] * (N) for _ in range(N)]
    
    def bfs(x,y):
        diractions = [(1,0),(0,1)]
        q = deque([(x,y)])
        visited[x][y] = grid[x][y]
        while q:
            x,y = q.popleft()
            for dx,dy in diractions:
                nx,ny = dx + x, dy + y
                if 0<= nx < N and 0<= ny < N:
                    if visited[nx][ny] > visited[x][y] + grid[nx][ny]:
                        visited[nx][ny] = visited[x][y] + grid[nx][ny]
                        q.append((nx,ny))
                        
    bfs(0,0)
    print(f"#{test_case} {visited[N-1][N-1]}")
                        
                
        