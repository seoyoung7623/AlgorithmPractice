#14503_로봇청소기 G5

# >> 다시 짠 코드
N,M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[r][c] = 1
cnt = 1

dr = [-1,0,1,0]
dc = [0,1,0,-1]


while 1:
    flag = 0
    for i in range(4):
        d = (d+3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if 0<= nr < N and nc < M and board[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                r = nr
                c = nc
                cnt +=1
                flag = 1
                break
    
    if flag == 0:
        if board[r - dr[d]][c - dc[d]] ==1:
            print(cnt)
            break
        else:
            r, c = r-dr[d],c-dc[d]
                



'''
N, M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
cnt = 1

visited = [[0]*M for i in range(N)]
visited[r][c] = 1

dr = [-1, 0, 1, 0] # 북 동 남 서 방향 -> 왼쪽 위가 1,1 이므로 상 하 좌표 주의!!
dc = [0, 1, 0, -1]

while 1:
    flag = 0 # 4방향을 돌았는지 확인용
    for i in range(4):
        d = (d+3)%4 ##시계반대 방향으로 한칸 돌림
        nr = r + dr[d]
        nc = c + dc[d]  # 그 방향으로 이동

        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:   # 벽으로 가지 안도록 처리
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                flag = 1
                break #다시 for 시작
    if flag == 0:
        if board[r - dr[d]][c - dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r - dr[d], c - dc[d]
'''


#     while d < 4:
#         x = r+dr[d]
#         y = c+dc[d]
#         move.append(board[x][y])
#         pre = back_trak(d)
#         d+=1
#         if board[x][y] == 0:
#             r = x
#             c = y
#             continue
#     if 0 not in move:
#         r = pre[0]
#         c = pre[1]
#         print("뒤로 이동:",r,c)
#         if move == [1,1,1,1]:
#             break
#         # for i in range(N):
#         #     if 0 not in board[i]:
#         #         break

# for i in range(N):
#     print(board[i])
# print(cnt)