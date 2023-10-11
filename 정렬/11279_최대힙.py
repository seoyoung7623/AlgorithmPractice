# 11279 최대 힙 S2
import sys
input = sys.stdin.readline # 시간 초과문제 발생
import heapq

N = int(input())
q = []
for i in range(N):
    num = int(input())
    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            print(-heapq.heappop(q))
    else:
        # 파이썬의 힙은 최소 힙으로 구현되어 있으므로 트랙을 이용해 최대 힙을 만든다. x, -x 
        heapq.heappush(q,-num)