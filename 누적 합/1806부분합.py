#1806 부분합
import sys
n,s = map(int,input().split())

numlist = list(map(int,input().split()))

numlist.sort()
numlist.reverse()
sum = 0
cnt = 0

for i in range(len(numlist)):
    if numlist[i] <= s and s>0:
        s = s - numlist[i]
        cnt+=1
    if s == 0:
        print(cnt)
        break
if s != 0:
    print(0)