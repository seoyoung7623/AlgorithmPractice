# 1715 카드 정렬하기 G4

import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
answer = 0

for _ in range(N):
    heapq.heappush(q,int(input()))
if len(q) == 1:
    print(0)
else:
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        answer += (a+b)
        heapq.heappush(q,a+b)
    print(answer)