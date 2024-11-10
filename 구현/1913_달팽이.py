# 1913 달팽이 S3
N = int(input())
grid = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
findNumber = int(input())
diractions = [[1,0],[0,1],[-1,0],[0,-1]]
x = 0
y = 0
number = N*N
grid[x][y] = number
visited[x][y] = True
answer = []
while number!=1:
    for dx,dy in diractions:
        while 1:
            if (number == findNumber):
                answer = [x+1,y+1]
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False:
                number -= 1
                grid[nx][ny] = number
                visited[nx][ny] = True
                x,y = nx,ny
            else:
                break
        if number == 1:
            break
for i in grid:
    print(*i)
print(*answer)
