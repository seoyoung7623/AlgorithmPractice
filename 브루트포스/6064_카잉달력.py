# 6064 카잉달력 S1 

# 틀렸습니다. + 1~ 전체 탐색은 시간 초과문제가 발생함
# def gcd(a,b):
#     while b > 0:
#         a,b = b,a%b
#     return a

# T = int(input())
# for _ in range(T):
#     M,N,x,y = map(int,input().split())
#     lcd = M*N//gcd(M,N)
#     for i in range(1,lcd+1):
#         if i % M == x and i % N == y or i % M == 0 and i % N == 0:
#             print(i)
#             break
#     else:
#         print(-1) 

# +M +N 해서 나머지가 같은 값
T = int(input())
for _ in range(T):
    M,N,x,y = map(int,input().split())
    f = 1
    while x <= M*N:
        if x % N == y % N: # x를 N으로 나누어주어 y와 같은지 확인
            print(x)
            f= 0
            break
        x += M
    if f:
        print(-1)