#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10994                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10994                          #+#        #+#      #+#     #
#    Solved: 2025/08/06 15:12:49 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
정사각형
1 5 9 13 +4씩 증가
n*4-3
'''
# 1. 구현 방식
N = int(input())

def draw_star(n,canvars):
    length = n*4-3
    for x in range(1,length//2):
        if x % 2 == 0:
            canvars[x] = canvars[x-1].copy()
            for y in range(x,length-x):
                canvars[x][y] = '*'
        if x % 2 == 1:
            for y in range(0,x,2):
                canvars[x][length-y-1] = '*'
                canvars[x][y] = '*'
    for y in range(0,length,2):
        canvars[length//2][y] = '*'
    for x in range(length//2,length):
        canvars[x] = canvars[length-x-1].copy()
    canvars[0],canvars[-1] = ['*']*length,['*']*length

length = N*4-3
canvars = [[' ' for _ in range(length)] for _ in range(length)]
draw_star(N,canvars)

for row in canvars:
    print(''.join(row).rstrip())

# 2. 재귀 방식
import sys
sys.setrecursionlimit(10000)

N = int(input())

def draw_star(n,x,y,canvars):
    length = n*4-3
    if n == 1:
        canvars[x][y] = '*'
        return
    for i in range(length):
        canvars[x][y+i] = '*'
        canvars[x+length-1][y+i] = '*'
    for i in range(length):
        canvars[x+i][y] = '*'
        canvars[x+i][y+length-1] = '*'
    draw_star(n-1,x+2,y+2,canvars)


length = N*4-3
canvars = [[' ' for _ in range(length)] for _ in range(length)]

draw_star(N,0,0,canvars)

for row in canvars:
    print(''.join(row).rstrip())


