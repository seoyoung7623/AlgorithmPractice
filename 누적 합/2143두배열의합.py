#2143 두 배열의 합
import bisect
import sys
input = sys.stdin.readline
t = int(input())
n = int(input())
nlist = list(map(int,input().split()))
m = int(input())
mlist = list(map(int,input().split()))
Nsum = []
Msum = []

for i in range(n):
    s = nlist[i]
    Nsum.append(s)
    for j in range(i+1,n):
        s += nlist[j]
        Nsum.append(s)
for i in range(m):
    s = mlist[i]
    Msum.append(s)
    for j in range(i+1,m):
        s += mlist[j]
        Msum.append(s)
Nsum.sort()
Msum.sort()
answer = 0
for i in range(len(Nsum)):#이분탐색
    l = bisect.bisect_left(Msum,t-Nsum[i])
    r = bisect.bisect_right(Msum,t-Nsum[i])
    answer += r-l
print(answer)

"""       
for i in range(len(nlist)):
    length = len(mlist)
    for j in range(length):
        num = nlist[i] + mlist[j]
        if num > t:
            continue
        else:
            mlist.append(num)
print(mlist.count(t))
"""
