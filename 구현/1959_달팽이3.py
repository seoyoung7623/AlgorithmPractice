# 1959 달팽이3 G3
# 메모리 제한과 너무 큰 범위를 보고 상하좌우 반복탐색은 시간이 초과할것
# 공식 추리문제
import sys
input = sys.stdin.readline
M,N = map(int,input().split())
grid = [[0]*N for _ in range(M)]
x = 0
y = 0
grid[x][y] = 1
toggle = False

def check(x,y):
    global toggle
    if (x+1==M or grid[x+1][y]==1) and (x-1<0 or grid[x-1][y]== 1) and (y+1==N or grid[x][y+1]==1) and (y-1 < 0 or grid[x][y-1]==1):
        toggle = True
        return True


# 종료조건 : 사방향에서 모두 이동할수없을때
# 우 하 좌 상
while 1:
    while y+1<N and grid[x][y+1] == 0:
        y += 1
        grid[x][y] = 1
        if check(x,y):
            answer = [x,y]
            break

    if toggle:
        break

    while x+1<M and grid[x+1][y] ==0:
        x+=1
        grid[x][y] = 1
        if check(x,y):
            answer = [x,y]
            break
    if toggle:
        break

    while y-1>=0 and grid[x][y-1]==0:
        y -= 1
        grid[x][y] = 1
        if check(x,y):
            answer = [x,y]
            break
    if toggle:
        break

    while x-1>=0 and grid[x-1][y]==0:
        x-=1
        grid[x][y] = 1
        if check(x,y):
            answer = [x,y]
            break
    if toggle:
        break

if M>N:
    print((N*2)-1)
else:
    print(N*2-2)
print(answer[0]+1,answer[1]+1)

