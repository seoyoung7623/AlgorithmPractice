# 11286 절댓값 힙 S1
import sys
import heapq

input = sys.stdin.readline
N = int(input())
q = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(q) == 0:
            print(0)
            continue
        _ , result = heapq.heappop(q)
        print(result)
    else:
        heapq.heappush(q,(abs(num),num)) # 1. abs(num)을 기준으로 힙 정렬 2. num을 기준으로 힙 정렬

