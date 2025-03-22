import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M,R = map(int,input().split())

grid = [[] for _ in range(N+1)]
answer = [0] * N
visited = [0] * N
cnt = 0

def dfs(R):
    global cnt
    visited[R-1] = 1
    cnt += 1
    answer[R-1] = cnt 
    arr = sorted(grid[R])
    for x in arr:
        if not visited[x-1]:
            dfs(x)

for i in range(M):
    u,v = map(int,input().split())
    grid[u].append(v)
    grid[v].append(u)

dfs(R)
for i in answer:
    print(i)