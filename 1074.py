# z

#재귀함수를 이용
# def sqareSet(N,r,c):
#     if N == 0:
#         return 0
#     return 2*(r%2)+(c%2) + 4*sqareSet(N-1,int(r/2),int(c/2))

# N,r,c = map(int,input().split())
# print(sqareSet(N,r,c))

#분할을 이용
N,r,c = map(int,input().split())
ans = 0

while N != 0:
    N -=1
    #1사분면
    if r< 2**N and c<2**N:
        ans += (2**N) * (2**N) * 0
    
    #2사분면
    elif r<2 **N and c >= 2** N:
        ans += (2**N) * (2 ** N) *1
        c -= (2**N) 
    
    elif r >= 2**N and c<2**N:
        ans += (2**N)*(2**N)*2
        r-=(2**N)

    else:
        ans +=(2**N) *(2**N)*3
        r -= (2**N)
        c -= (2**N)
print(ans)
