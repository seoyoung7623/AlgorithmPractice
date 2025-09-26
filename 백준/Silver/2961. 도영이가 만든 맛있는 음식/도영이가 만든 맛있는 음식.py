from itertools import combinations
import sys
input = sys.stdin.readline
MAX = 1e9

N = int(input())

lst = []
answer = MAX
for _ in range(N):
    S,B = map(int,input().split())
    lst.append((S,B))

for i in range(1,N+1):
    cases = combinations(range(N),i)

    for case in cases:
        s,b = 1,0
        for j in range(len(lst)):
            if j in case:
                s *= lst[j][0]
                b += lst[j][1]
        answer = min(answer, abs(s-b))

print(answer)