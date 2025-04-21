import sys
input = sys.stdin.readline

N,M = map(int,input().split())
grid1 = [list(map(int,input().split())) for _ in range(N)]
grid2 = [list(map(int,input().split())) for _ in range(N)]
answer = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        answer[i][j] = grid1[i][j] + grid2[i][j]

for i in range(N):
    print(*answer[i])
