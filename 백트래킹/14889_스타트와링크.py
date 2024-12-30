#14889 스타트와 링크 S2

# N = int(input())
# board = [list(map(int,input().split())) for _ in range(N)]
# visited = [False for _ in range(N)]
# INF = 2147000000
# res = INF

# def DFS(L,idx):
#     global res
#     if L == N//2:
#         A = 0
#         B = 0
#         for i in range(N):
#             for j in range(N):
#                 if visited[i] and visited[j]: #방문한 경우라면
#                     A += board[i][j]
#                 elif not visited[i] and not visited[j]: #방문하지 않은 경우라면
#                     B += board[i][j]
#         res = min(res,abs(A-B))
#         return
#     for i in range(idx,N):
#         if not visited[i]:
#             visited[i] = True
#             DFS(L+1,i+1)
#             visited[i] = False
# DFS(0,0)
# print(res)

''' 백트래킹 풀이
backtacking(L+1,i+1) 이부분에서 i를 idx로 설정해서 시간초과가 남..
'''
import sys
input = sys.stdin.readline

N = int(input())
table = [list(map(int,input().split())) for _ in range(N)]
visited = [0]*N
min_diff = 1e5

def backtacking(L,idx):
    global min_diff
    if L == N//2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i]== 1 and visited[j] == 1:
                    A += table[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    B += table[i][j]
        min_diff = min(abs(A-B),min_diff)
        return
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = 1
            backtacking(L+1,i+1)
            visited[i] = 0
backtacking(0,0)
print(min_diff)


