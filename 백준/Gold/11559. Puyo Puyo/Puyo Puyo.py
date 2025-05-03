from collections import deque
grid = [list(input()) for _ in range(12)]
turn_grid = [[0]*12 for _ in range(6)]
for i in range(12):
    for j in range(6):
        turn_grid[j][11-i] = grid[i][j]

diractions = [(1,0),(0,1),(-1,0),(0,-1)]
def BFS(x,y,visited):
    q = deque([(x,y)])
    color = turn_grid[x][y]
    cnt=1
    puyo = [(x,y)]
    while q:
        x,y = q.popleft() #세로,가로
        for dx,dy in diractions:
            nx = x + dx
            ny = y + dy
            if 0<=nx<6 and 0<=ny<12 and visited[nx][ny] == 0 and turn_grid[nx][ny] == color:
                cnt+=1
                visited[nx][ny] = 1
                q.append((nx,ny))
                puyo.append((nx,ny))
    return cnt,puyo

def descent():
    for i in range(6):
        arr = []
        for j in range(12):
            if turn_grid[i][j] != '.':
                arr.append(turn_grid[i][j])
        if arr:
            turn_grid[i] = arr+['.']*(12-len(arr))

def dump(puyo):
    for x,y in puyo:
        turn_grid[x][y] = '.'


toggle = True
answer = 0
while True:
    if not toggle:
        break
    toggle = False
    visited = [[0]*12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if turn_grid[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                cnt,puyo = BFS(i,j,visited)
                if cnt>=4:
                    toggle = True
                    dump(puyo)
                    
    if toggle:
        answer += 1
        descent()
print(answer)