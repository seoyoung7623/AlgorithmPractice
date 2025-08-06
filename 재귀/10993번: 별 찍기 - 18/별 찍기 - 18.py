#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10993                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10993                          #+#        #+#      #+#     #
#    Solved: 2025/08/05 15:36:07 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
<내 접근>
홀수이면 삼각형
짝수이면 역삼각형

높이, 너비의 규칙을 찾는다.
'''

'''
<정답 풀이>
캔버스 밑그림을 그리고(크기 결정),
별을 추가한다. 별은 양쪽으로 H-1으로 별을 추가한다.
최대 별의 개수: 2^(n+1)-3 너비

H = 2**N - 1
W = 2**(N+1) - 3

안에 삼각형은 높이의 절반
'''

# import sys
# sys.setrecursionlimit(10000)

# def draw(n, x, y, canvas):
#     if n == 1:
#         canvas[x][y] = '*'
#         return

#     height = 2**n - 1
#     width = 2**(n+1) - 3

#     if n % 2 == 1:
#         # 정삼각형 (▲)
#         for i in range(height):
#             canvas[x + i][y - i] = '*'
#             canvas[x + i][y + i] = '*'
#         for j in range(-height+1, height):
#             canvas[x + height - 1][y + j] = '*' # 가장 긴 별 길이 채우기
#         # 내부 삼각형 호출
#         draw(n - 1, x + height // 2, y, canvas)
#     else:
#         # 역삼각형 (▼)
#         for i in range(height):
#             canvas[x + i][y + (width//2) - i] = '*'
#             canvas[x + i][y - (width//2) + i] = '*'
#         for j in range(-height+1, height):
#             canvas[x][y + j] = '*' # 가장 긴 별 길이 채우기
#         # 내부 삼각형 호출
#         draw(n - 1, x + 1, y, canvas)

# def main():
#     N = int(input())
#     H = 2**N - 1
#     W = 2**(N+1) - 3
#     # 일단 밑그림 크기부터 결정
#     canvas = [[' ' for _ in range(W)] for _ in range(H)]

#     # 시작 위치
#     if N % 2 == 1: # 홀수
#         draw(N, 0, W // 2, canvas) # N번째, 세로, 가로, 캔버스
#     else: # 짝수
#         draw(N, 0, W // 2, canvas)

#     for row in canvas:
#         print(''.join(row).rstrip())

# main()

import sys
sys.setrecursionlimit(10000)

N = int(input())

def draw_star(n,x,y,canvas):
    if n == 1:
        canvas[x][y] = '*'
        return

    W = 2**(n+1)-3
    H = 2**n-1

    if n % 2 == 0: # 짝수인경우
        for i in range(H):
            canvas[x+i][y+(W//2)-i] = '*'
            canvas[x+i][y-(W//2)+i] = '*'
        for j in range(-H+1, H):
            canvas[x][y+j] = '*'
        draw_star(n-1,x+1,y,canvas)
    else:
        for i in range(H):
            canvas[x+i][y-i] = '*'
            canvas[x+i][y+i] = '*'
        for j in range(-H+1, H):
            canvas[x+H-1][y+j] = '*'
        draw_star(n-1,x+H//2,y,canvas)

def main(n):
    W = 2**(n+1)-3
    H = 2**n-1

    canvas = [[' ' for _ in range(W)] for _ in range(H)]

    draw_star(n,0,W//2,canvas)

    for row in canvas:
        print(''.join(row).rstrip())

main(N)