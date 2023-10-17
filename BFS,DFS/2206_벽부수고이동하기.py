# 2206 벽 부수고 이동하기 G3 
# from collections import deque

# N,M = map(int,input().split())
# graph = [list(map(int,input())) for _ in range(N)]
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def BFS(graph,visited):
#     q = deque()
#     q.append((0,0))
#     visited[0][0] = 1
#     flag = False
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0<=nx<M and 0<= ny<N and visited[ny][nx] == 0 and graph[ny][nx] != 1:
#                 visited[ny][nx] = visited[y][x] + 1
#                 if nx == M-1 and ny == N-1:
#                     flag = True
#                     return visited[N-1][M-1]   
#                 q.append((nx,ny))

# toggle = False

# result = []
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             graph[i][j] = 0
#             visited = [[0]*M for _ in range(N)]
#             cnt = BFS(graph,visited)
#             if cnt:
#                 result.append(cnt)
#             graph[i][j] = 1

# print(min(result) if result else -1)

# 3차원 배열로 접근

from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
# 3차원리스트(행, 열, 벽을 깬 여부) 생성
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y,wall_break_left,visited,graph):
    q = deque()
    q.append((x,y,wall_break_left))
    visited[x][y][wall_break_left] = 1
    while q:
        x,y,wall_break_left = q.popleft()
        if x == n-1 and y == m-1: #종료조건
            return visited[x][y][wall_break_left]
        
        for i in range(4): #이동할 4방향
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 부수지 않고 이동
                if graph[nx][ny] == 0 and visited[nx][ny][wall_break_left] == 0:
                    q.append((nx,ny,wall_break_left))
                    visited[nx][ny][wall_break_left] = visited[x][y][wall_break_left] + 1
                # 벽을 부수고 이동 -> 어차피 벽은 하나밖에 못뚜니까 초기 위치에서 이동가능한 가까운 하나만 뚫으면 됨!
                if graph[nx][ny] == 1 and wall_break_left == 1:
                    q.append((nx,ny,wall_break_left - 1))
                    visited[nx][ny][wall_break_left-1] = visited[x][y][wall_break_left] + 1 # 부순거는 안부순거에서 +1
    return -1
            
print(BFS(0,0,1,visited,graph))