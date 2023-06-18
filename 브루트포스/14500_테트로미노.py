# 14500 테트로미노
'''
앞에 4가지 도형은 DFS를 이용해 값을 계산한다.
'''
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

move=[(0,1),(0,-1),(1,0),(-1,0)] # 상하좌우
maxValue = 0

def dfs(i,j,dsum,cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue,dsum)
        return


    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]  
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni,nj,dsum + board[ni][nj],cnt + 1)
            visited[ni][nj] = False

def exce(i,j):
    global maxValue
    for n in range(4):
        tmp = board[i][j]
        for k in range(3):
             # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301 -> n으로 인해서 4가지로 나올수 있음
            t = (n+k)%4 
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0 <= ni < N and 0 <= nj <M):
                tmp = 0 # 초기화
                break
            tmp += board[ni][nj]
        maxValue = max(maxValue,tmp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,board[i][j],1)
        visited[i][j] = False

        exce(i,j)
print(maxValue)


'''
# 나 왜 BFS로 접근했니.. DFS랑 헷갈리지 말것!!
    while q:
        x,y = q.popleft()
        sum += board[x][y]
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            else:
                q.append(nx,ny)

while 1:
    q = deque()
    q.append

for i in range(N):
    for j in range(M):
        q = deque()
        q.append(i,j)    
        sum = 0
        sum = board[i][j]
        for k in range(4):
            i = i+dy[k]
            j = j+dx[k]
            sum += board[i][j]
            for z in range(4):
                sum += board[i][j]
                i = i+dy[z]
                j = j+dx[z]
                # sum = board[i+dy[z]][j+dx[z]]


'''
        