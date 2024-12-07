# 2167 2차원 배열의 합
'''
1. (i,j)부터 (x,y)까지 더하기
10^5개의 숫자
횟수 10^4
1초정도 나올듯

시간 초과 안날듯

 = DP를 이용해 합을 저장한다.
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(list(map(int,input().split())) for _ in range(N))
sum_arr = list([0]*(M+1) for _ in range(N+1))
sum_arr[1][1] = arr[0][0]

for i in range(1,N+1):
    for j in range(1,M+1):
        sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]
T = int(input())    

for test_case in range(T):
    sum = 0
    i,j,x,y = map(int,input().split())
    sum = sum_arr[x][y] - sum_arr[x][j-1] - sum_arr[i-1][y] + sum_arr[i-1][j-1]
    print(sum)
