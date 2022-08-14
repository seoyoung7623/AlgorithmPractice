#1018 체스판 다시 칠하기
#세로 m 가로 n
m,n = map(int,input().split())
yplus = 0
cnt = 0

for i in range(plus,m):
    li = list(input())
    xplus = 0
    for j in range(xplus,8+xplus):
        if xplus+8 == n:
            break
        if li[j] == li[j+1]:
            cnt +=1
        xplus +=1 #위치 어디 줄? 루프 밖? 안?