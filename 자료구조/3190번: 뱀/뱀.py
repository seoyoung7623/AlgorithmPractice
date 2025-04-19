#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3190                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3190                           #+#        #+#      #+#     #
#    Solved: 2025/04/19 23:13:23 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
몸 길이에 걸리는 경우
몸 위치를 어떻게 저장할 것인가 -> 큐 FILO
'''
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
K = int(input())
grid = [[0]*N for _ in range(N)]
for k in range(K):
    x,y = map(int,input().split())
    grid[x-1][y-1] = 1

L = int(input())
d_change = deque([])
for l in range(L):
    t,d = input().split()
    d_change.append((int(t),d))

x,y = 0,0
time = 0
snake_body = deque([(0,0)])
diractions = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0
while True:

    dx,dy = diractions[d]
    nx = x + dx
    ny = y + dy
    time += 1
    
    if 0>nx or nx>=N or 0>ny or ny>=N:
        break
    if (nx,ny) in snake_body:
        break
    
    snake_body.append((nx,ny))
    if grid[nx][ny] == 1: # 열매가 있는 경우
        grid[nx][ny] = 0 
    else:
        snake_body.popleft()
        
    if d_change and d_change[0][0] == time:
        if d_change[0][1] == 'D':
            d = (d + 1) % 4
        elif d_change[0][1] == 'L':
            d = (d + 3) % 4
        d_change.popleft()
    x,y = nx,ny
        
    
print(time)