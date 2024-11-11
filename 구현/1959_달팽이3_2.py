# 1959 달팽이3 G3
# 반복문에서 일반화를 적용한 코드
# 구현 공식 추리문제
import sys
input = sys.stdin.readline
M,N = map(int,input().split())

# 회전개수
if M > N:
    print(2 * (N - 1) + 1)
else:
    print(2 * (M - 1))

# 좌표 출력
if (M==N): #N*N
    if(N%2!=0): # 홀수
        print(f"{M//2+1} {N//2+1}")
    else: # 짝수
        print(f"{M//2+1} {N//2}")
else:
    if(N>M):
        if(M%2!=0):
            print(f"{M//2 + 1} {(M//2)+1+(N-M)}")
        else: # 행이 짝수인 경우
            print(f"{M//2+1} {M//2}")
    else: # 열이 홀수인 경우
        if(N%2!=0):
            print(f"{N//2+1+(M-N)} {N//2+1}")
        else: 
            print(f"{N//2+1} {N//2}")
    
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

# 회전 개수 계산
if M > N:
    print(2 * (N - 1) + 1)
else:
    print(2 * (M - 1))

# 좌표 계산
if M == N:  # N x N 정사각형
    if M % 2 == 1:  # 홀수 크기 정사각형
        print((M - 1) // 2 + 1, (M - 1) // 2 + 1)
    else:  # 짝수 크기 정사각형
        print(M // 2 + 1, M // 2)
else:
    if N > M:
        if M % 2 == 0:  # M이 짝수인 경우
            print(M // 2 + 1, M // 2)
        else:  # M이 홀수인 경우
            print(M // 2 + 1, M // 2 + 1 + (N - M))
    else:  # N < M
        if N % 2 == 0:  # N이 짝수인 경우
            print(N // 2 + 1, N // 2)
        else:  # N이 홀수인 경우
            print(N // 2 + 1 + (M - N), N // 2 + 1)
