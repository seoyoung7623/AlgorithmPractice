#2630 색종이 만들기 S2 - 분할, 재귀
N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
w_cnt = 0 #0 표시
b_cnt = 0 #1 표시

def cut(x,y,N): #x,y 는 0,0 초기 값!!
    global w_cnt, b_cnt
    color = paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color != paper[i][j]:
                cut(x,y,N//2)
                cut(x,y+N//2,N//2)
                cut(x+N//2,y,N//2)
                cut(x+N//2,y+N//2,N//2)
                return
    if color == 0:
        w_cnt += 1
    elif color == 1:
        b_cnt += 1

cut(0,0,N)
print(w_cnt)
print(b_cnt)
            


# def cut(x,y,N):
#     # if N == 1:
#     for i in range(N):
#         for j in range(N):
#             sum = 0
#             if i <= (N//2) and j <= (N//2):
#                 sum += paper[i][j]
#             if sum == (N//2) * (N//2):
#                 b_cnt += 1
#             elif sum == 0:
#                 w_cnt += 1
#             else:
#                 cut(0,0,N//2)
#             sum = 0 
#             if y <= i < (N//2) and (N//2) < j < N:
#                 sum += paper[i][j]
#             if sum == (N//2) * (N//2):
#                 b_cnt += 1
#             elif sum == 0:
#                 w_cnt += 1
#             else:
#                 cut(N//2) 