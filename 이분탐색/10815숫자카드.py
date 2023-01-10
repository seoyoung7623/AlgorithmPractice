#10815 숫자카드
import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int,input().split()))
m = int(input())
mlist = list(map(int,input().split()))
nlist.sort()
ans = []

def binary(s,start,end):
    while start <= end:
        min = (start + end)//2
        if nlist[min] == s:
            return 1
        elif nlist[min] < s:
            start = min+1
        else:
            end = min - 1
    return 0

for i in mlist:
    print(binary(i,0,n-1),end=' ')

