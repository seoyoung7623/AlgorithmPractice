#1806 부분합
'''
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
    '''
#문제를 잘못이해했다. S이상의 수임!
import sys

n,s = map(int,input().split())
numlist = list(map(int,input().split()))

left,right = 0,0
sum = 0
minlength = sys.maxsize

while 1:
    if sum >= s:
        minlength = min(minlength,right-left)
        sum -= numlist[left]
        left +=1
    elif right == n:
        break
    else:
        sum +=numlist[right]
        right +=1
if minlength == sys.maxsize:
    print(0)
else:
    print(minlength)
