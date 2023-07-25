# # 14499 주사위굴리기 G4
N,M,x,y,K = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
resert = list(map(int,input().split()))
dice = list([0]*6)

def board(x,y):
    if(0<=x<M and 0<=y<N):
        return True
    else:
        return False

for i in range(K):
    dice2 = dice.copy()
    if resert[i] == 1: #동
        if not board(x+1,y):
            continue
        x += 1
        dice[0] = dice2[3]
        dice[2] = dice2[0]
        dice[3] = dice2[5]
        dice[5] = dice2[2]
        if graph[y][x] == 0:
            graph[y][x] = dice[5]
        else:
            dice[5] = graph[y][x]
            graph[y][x] = 0
    elif resert[i] == 2: #서
        if not board(x-1,y):
            continue
        x -= 1
        dice[0] = dice2[2]
        dice[2] = dice2[5]
        dice[3] = dice2[0]
        dice[5] = dice2[3]
        if graph[y][x] == 0:
            graph[y][x] = dice[5]
        else:
            dice[5] = graph[y][x]
            graph[y][x] = 0
    elif resert[i] == 3: #북      
        if not board(x,y-1):
            continue
        y -=1
        dice[0] = dice2[1]
        dice[1] = dice2[5]
        dice[4] = dice2[0]
        dice[5] = dice2[4]
        if graph[y][x] == 0:
            graph[y][x] = dice[5]
        else:
            dice[5] = graph[y][x]
            graph[y][x] = 0
    else: #남
        if not board(x,y+1):
            continue
        y +=1
        dice[0] = dice2[4]
        dice[1] = dice2[0]
        dice[4] = dice2[5]
        dice[5] = dice2[1]
        if graph[y][x] == 0:
            graph[y][x] = dice[5]
        else:
            dice[5] = graph[y][x]
            graph[y][x] = 0
    print(dice[0])


    
'''
import sys
input = sys.stdin.readline

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0] * 6

for d in command:
    nx = x + dr[d]
    ny = y + dc[d]

    if not 0 <= nx < n or not 0 <= ny < m:      ## 범위 밖에 있는 좌표면 continue
        continue

    ## 헷갈리기 때문에 방향으로 명시해줌
    east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    ### 방향에 따라 주사위 굴리기~~~!!
    if d == 1:
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif d == 3:
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    elif d == 4:
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north

    ## 지도에 숫자가 0일 때
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[5]
    ## 지도의 숫자가 0이 아닐 때
    else:
        dice[5] = maps[nx][ny]
        maps[nx][ny] = 0

    ## 꼭 값을 갱신해주기!
    x, y = nx, ny
    print(dice[4])


'''
