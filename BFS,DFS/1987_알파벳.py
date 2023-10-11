# 1987 알파벳 G4
# from collections import deque
import sys
input = sys.stdin.readline

R,C = map(int,input().split())
board = [list(map(lambda x:ord(x)-65, input())) for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0
visited = set() # 알파벳 방문기록
         
def DFS(x,y,cnt):
    global ans
    ans = max(ans,cnt)
    
    for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]

         if 0<= nx < C and 0 <= ny < R and not board[ny][nx] in visited:
              visited.add(board[ny][nx])
              DFS(nx,ny,cnt + 1)
              visited.remove(board[ny][nx])
    
        
visited.add(board[0][0])
DFS(0,0,1)
print(ans)


# result = [[1]*C for _ in range(R)]
# box = []
# answer = []

# box에 기록하는게 겹치는 문제 bfs말고 dfs로 접근해야한다.
# def bfs():
#     q = deque()
#     q.append((0,0))
#     box.append(board[0][0])
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (nx<0 or nx>=C or ny<0 or ny>= R) or board[ny][nx] in box:
#                 continue
#             box.append(board[ny][nx])
#             q.append((nx,ny))
#             result[ny][nx] = max(result[ny][nx],result[y][x]+1)

# def DFS(x,y,box):
#     box.append(board[y][x]) 
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if (nx<0 or nx>=C or ny<0 or ny>= R) or board[ny][nx] in box:
#                 continue
#         result[ny][nx] = max(result[ny][nx],result[y][x]+1)
#         DFS(nx,ny,box) # DFS를 수행할 조건은 방문하지 않을 알파벳이여야한다.
#     box.pop()
#         answer.append(result[nx][ny])
        