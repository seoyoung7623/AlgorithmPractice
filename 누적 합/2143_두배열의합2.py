#2143 두 배열의 합
'''
이분탐색이용
부배열의합에 동일 값을 찾기 위한 이분탐색!
'''
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

# N 부배열합
for i in range(n):
    s = nlist[i]
    Nsum.append(s)
    for j in range(i+1,n):
        s += nlist[j]
        Nsum.append(s)

# M 부배열합
for i in range(m):
    s = mlist[i]
    Msum.append(s)
    for j in range(i+1,m):
        s += mlist[j]
        Msum.append(s)

Nsum.sort()
Msum.sort()
answer = 0
'''
그 부분합의 개수를 구하기 위한 이분탐색
'''
for i in range(len(Nsum)): #이분탐색
    l = bisect.bisect_left(Msum,t-Nsum[i])
    r = bisect.bisect_right(Msum,t-Nsum[i])
    answer += r-l # 동일값의 개수
print(answer)
