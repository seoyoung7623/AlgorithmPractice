# 1072 게임 S3
X,Y = map(int,input().split())
Z = (Y*100)//X
min_cnt = 0
max_cnt = X+1
answer = 0

if Z>= 99:
    print(-1)
else:
    # 아 while문에 같음이 없으면 max는 mid로 지정 mid-1 아님
    # 그리고 정답은 min
    while min_cnt <= max_cnt: #여기랑
        mid = min_cnt + (max_cnt-min_cnt)//2
        rate = (100*(Y+mid))//(X+mid)
        if rate > Z:
            answer = mid
            max_cnt = mid - 1 # 여기 세트
        else:
            min_cnt = mid + 1
    print(answer)
