# 16236 아기상어 G3
'''
https://www.acmicpc.net/problem/16236
BFS로 상어가 이동 가능한 범위를 탐색.
먹을 물고기를 후보로 정렬하여 가장 가까운 물고기를 선택.
상어가 물고기를 먹으며 크기를 증가시킴.
'''

from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
pos = [] #시작위치 지정
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            pos.append(i)
            pos.append(j)

def bfs(x,y): #x,y는 현재 상어의 위치
    visited = [[0]*N for _ in range(N)]
    queue = deque([[x,y]]) #초깃값 설정
    cand = [] #

    visited[x][y] = 1

    while queue: # 상어가 이동할수 있는 곳을 판단
        i,j = queue.popleft()

        for idx in range(4):
            ii,jj = i + dx[idx], j + dy[idx]
            if 0 <= ii < N and 0 <= jj < N and visited[ii][jj] == 0: #범위체크
                if graph[x][y] > graph[ii][jj] and graph[ii][jj] != 0:  #x,y는 현재 상어의 위치 / 상어의 크기보다 작은경우 0은 아닌경우 / 물고기를 먹음
                    visited[ii][jj] = visited[i][j] + 1 #이동 
                    cand.append((visited[ii][jj]-1,ii,jj))
                elif graph[x][y] == graph[ii][jj]:
                    visited[ii][jj] = visited[i][j] + 1 #이동 
                    queue.append([ii,jj])
                elif graph[ii][jj] == 0:
                    visited[ii][jj] = visited[i][j] + 1 #이동 
                    queue.append([ii,jj])
                
    # 후보리스트
    return sorted(cand,key = lambda x :(x[0],x[1],x[2]))


cnt = 0
i,j = pos
size = [2,0]
while True:
    graph[i][j] = size[0]
    queue = deque(bfs(i,j)) #후보리스트 초기값으로 넣어줌

    if not queue: #큐가 비어있다면
        break

    # 후보리스트가 나오면 맨 앞의 후보 먹이를 뽑아 위치로 이동
    # 가장 가까운 물고기 선택
    step,xx,yy = queue.popleft()
    cnt += step #이동한 시간
    size[1] +=1 # 먹이를 먹음

    # 사이즈 체크 상어가 커지는 순간
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    graph[i][j] = 0 #다음 bfs를진행할때는 초기 위치 삭제
    i,j = xx,yy #이동한 위치
print(cnt)
