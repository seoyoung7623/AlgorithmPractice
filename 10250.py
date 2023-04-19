#10250 ACM 호텔
T = int(input())

for i in range(T):
    H,W,N = list(map(int,input().split()))        

    f = N%H
    s = N // H +1

    if (f==0):
        f = H
        s = N//H

    print(f"{f*100+s}")

    # 내가 틀린 코드
    # print(f"{f}0{s}") 
    # 중간에 0을 추가하는것이 아님. 십의 자리까지 방의 번호인걸 생각하지 못했음