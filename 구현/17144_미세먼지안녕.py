# 17144 미세먼지 안녕! G4
'''
구현
그래프 한칸씩 회전 로직 -> 그래프 탐색 dx,dy를 만들어서 벽을 부딫히면 탐색 방향을 바꿈
'''
R,C,T = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
up = -1
down = -1
for i in range(R):
    if board[i][0] == -1:
        up = i
        down = i+1
        break

# 확산
def diffusion():
    global board,up,down
    visited = [[0]*C for _ in range(R)]
    visited[up][0],visited[down][0] = -1,-1
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                round = board[i][j]//5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0<=nx<R and 0<=ny<C and board[nx][ny] != -1:
                        visited[nx][ny] += round
                        board[i][j] -= round
                visited[i][j] += board[i][j]
        
    board = visited[:]

# 공기청정기 위쪽 이동
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny

for _ in range(T):
    diffusion()
    air_up()
    air_down()
answer = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            answer += board[i][j]
print(answer)