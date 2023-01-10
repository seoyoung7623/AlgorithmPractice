#10816 숫자카드 2
import sys
import bisect
input = sys.stdin.readline

n = int(input())
nlist = list(map(int,input().split()))
m = int(input())
mlist = list(map(int,input().split()))
nlist.sort()
ans = []

for i in mlist:
    r = bisect.bisect_right(nlist,i)
    l = bisect.bisect_left(nlist,i)
    ans.append(r-l)

for i in ans:
    print(i,end=' ')


################################
## 해쉬 알고리즘 방식 Dicrionary
'''
from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))
'''