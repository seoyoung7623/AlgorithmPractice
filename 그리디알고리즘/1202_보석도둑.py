# 1202 보석도둑 G1
'''
보석 개수N, 가방 개수K
가방에는 보석을 하나씩만 무게 M 가격V
가방순서대로 들어갈 수 있는 보석을 찾는데 (최소힙)
가능한 보석중에서 가장 가치가 높은것을 찾는다. (최대힙))
'''
import heapq
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
jew = []
for _ in range(N):
    heapq.heappush(jew,list(map(int,input().split())))
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()

total = 0
jew_tem = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(jew_tem,-heapq.heappop(jew)[1])
    if jew_tem:
        total += -heapq.heappop(jew_tem)

print(total)
