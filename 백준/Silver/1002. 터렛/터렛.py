T = int(input())
for test_case in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    cnt = 0
    d = ((x1-x2)**2+(y1-y2)**2)**0.5

    # 중심이 같은 경우
    if d == 0 and r1 == r2:
        cnt = -1
    elif d == 0 and r1 != r2:
        cnt = 0
    elif d == abs(r1-r2): # 내접
        cnt = 1
    elif d == r1+r2: # 외접
        cnt = 1
    elif abs(r1-r2) > d: # 원안에 원
        cnt = 0
    elif r1+r2 < d: # 원이 만나지 않음
        cnt = 0
    else:
        cnt = 2
    print(cnt)
            