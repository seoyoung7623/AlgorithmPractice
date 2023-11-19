# 16924 십자가 찾기 S2
n,m = map(int,input().split())
board = [list(input()) for _ in range(n)] 
visited = [[0]*m for _ in range(n)]
result = []
for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            visited[i][j] = 1
for x in range(n):
    for y in range(m):
        s = 0
        flag = False
        if board[x][y] != '*': # 1.현재 위치도 '*' 십자가 # 2.이조건 안써서 틀림
            continue
        while 1:
            s += 1
            dx = [s,-s,0,0]
            dy = [0,0,s,-s]
            for k in range(4):
                nx,ny = x + dx[k] , y + dy[k]
                if 0> nx or nx>= n or ny<0 or ny >= m:
                    flag = True
                    break
                if board[nx][ny] == '.':
                    flag = True
                    break
            else:
                visited[x][y] = 0
                for i in range(4):
                    visited[x+dx[i]][y+dy[i]] = 0
                result.append((x+1,y+1,s))
            if flag:
                break

check = True
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            print(-1)
            check = False
            break
    if not check:
        break
if check:
    print(len(result))
    result.sort(key=lambda x: (x[0], x[1], -x[2]))
    for node in result:
        print(*node)