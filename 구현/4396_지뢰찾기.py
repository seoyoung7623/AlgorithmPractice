# 4396 지뢰찾기 S4
N = int(input())
grid = [list(input()) for _ in range(N)]
player = [list(input()) for _ in range(N)]
bumbs = []
flag = False
for i in range(N):
    for j in range(N):
        if grid[i][j] == '*':
            bumbs.append((i,j))

direction = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

for i in range(N):
    for j in range(N):
        if player[i][j] == 'x':
            if grid[i][j] == '*':
                flag = True
            player[i][j] = 0
            for dx,dy in direction:
                nx = i + dx
                ny = j + dy
                if 0<=nx<N and 0<=ny<N:
                    if grid[nx][ny] == '*':
                        player[i][j] += 1

if flag:
    for bx,by in bumbs:
        player[bx][by] = '*'

for i in range(N):
    for j in range(N):
        print(player[i][j],end='')
    print()