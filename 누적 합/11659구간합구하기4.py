# 11659 구간합구하기
# 1차원 배열
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
numlist = list(map(int,input().split()))

sumlist = [0]*(n+1)


for i in range(1,n+1):
    sumlist[i] = sumlist[i-1]+numlist[i-1]

for _ in range(m):
    i,j = map(int,input().split())
    print(sumlist[j]-sumlist[i-1])

