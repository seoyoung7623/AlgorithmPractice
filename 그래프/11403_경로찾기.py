# 11403 경로 찾기 S1
# from collections import deque
# import sys
# input = sys.stdin.readline

# N = int(input())
# graph = [list(map(int,input().split())) for _ in range(N)]
# result = [[0]*N for _ in range(N)]

# # 1. BFS 방법
# def bfs(x):
#     q = deque()
#     q.append(x)
#     check = [0 for _ in range(N)]
#     while q:
#         y = q.popleft()
#         for i in range(N):
#             if check[i] == 0 and graph[y][i] == 1:
#                 q.append(i)
#                 check[i] = 1
#                 result[x][i] = 1

# for i in range(N):
#     bfs(i)
# for i in result:
#     print(*i)

# 2. DFS 방법
# from collections import deque
# import sys
# input = sys.stdin.readline

# N = int(input())
# graph = [list(map(int,input().split())) for _ in range(N)]
# result = [0 for _ in range(N)]
# def dfs(x):
#     for i in range(N):
#         if graph[x][i] == 1 and result[i] == 0:
#             result[i] = 1
#             dfs(i)

# for i in range(N):
#     dfs(i)
#     for j in range(N):
#         if result[j] == 1:
#             print(1,end=' ')
#         else:
#             print(0,end=' ')
#     print()
#     result = [0 for _ in range(N)]

# 플로이드 워셜
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
    
for g in graph:
    print(*g)