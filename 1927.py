# 1927 최소 힙
# 자료 구조, 우선순위 큐
import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap,num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
"""
파이썬 heapq 모듈을 사용하면 쉽게 구할 수 있다. 
힙 정렬에 대한 이해도가 된 상태에서 사용하는 걸 권장! 
시간복잡도는 O(log2n)
"""