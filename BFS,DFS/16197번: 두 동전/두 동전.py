#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16197                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16197                          #+#        #+#      #+#     #
#    Solved: 2025/04/28 09:29:52 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
두 동전이 동시에 이동
두 동전 중 하나만 떨어뜨려야한다.
1. 좌표로 이동, BFS
동전 위치 visited 복수객체이기때문에 set()이 빠름

1. 두 동전 위치와 버튼을 누른 횟수를 큐에 저장한다. 
2. 이동 조건 처리 벽인지 떨어지는지
3. 종료 조건: 모두 떨어지거나 10번 초과 -1
'''
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split()) # 세로, 가로
board = [list(input()) for _ in range(N)]
walls = set()
coins = []

diractions = [(1,0),(0,1),(-1,0),(0,-1)]

def is_inside(x,y):
    return 0<=x<N and 0<=y<M

def bfs():
    q = deque()
    x1,y1 = coins[0]
    x2,y2 = coins[1]
    visited = set()
    q.append((x1,y1,x2,y2,0))
    visited.add((x1,y1,x2,y2))
    while q:
        x1,y1,x2,y2,cnt = q.popleft()
        if cnt >= 10:
            return -1
        for dx,dy in diractions:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy

            fall1 = not is_inside(nx1,ny1)
            fall2 = not is_inside(nx2,ny2)

            if fall1 and fall2:
                continue
            if fall1 or fall2:
                return cnt + 1
            
            # 벽이면 이동할 수 없음
            if board[nx1][ny1] == '#':
                nx1,ny1 = x1, y1
            if board[nx2][ny2] == '#':
                nx2,ny2 = x2, y2
            
            if (nx1,ny1,nx2,ny2) not in visited:
                visited.add((nx1,ny1,nx2,ny2))
                q.append((nx1,ny1,nx2,ny2,cnt+1))
    return -1
            
            
# 동전 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i,j))
            board[i][j] = '.'
            
        
print(bfs())
