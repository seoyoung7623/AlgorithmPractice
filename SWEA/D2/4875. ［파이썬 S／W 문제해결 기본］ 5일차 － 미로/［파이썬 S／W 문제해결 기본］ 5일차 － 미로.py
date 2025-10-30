

# import sys


'''
2 -> 3
'''
# sys.stdin = open("input.txt", "r")
from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int,input().strip())) for _ in range(N)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    valid = False
    
    def bfs(x,y):
        visited = [[0]*N for _ in range(N)]
        visited[x][y] = 1
        q = deque([(x,y)])
        
        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                nx, ny = x + dx, y + dy
                if 0<= nx < N and 0<= ny < N and visited[nx][ny] == 0 and grid[nx][ny] != 1:
                    if grid[nx][ny] == 3:
                        return True
                    visited[nx][ny] = 1
                    q.append((nx,ny))
        return False
       
        
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                if bfs(i,j):
                    print(f"#{test_case} 1")
                else:
                    print(f"#{test_case} 0")
    