# 1504 특정한 최단 경로 G4 
# 다익스트라 알고리즘
'''
v1,v2를 반드시 거쳐야하기 때문에 
start → v1 / v1 → v2 / v2 → end
start → v2 / v2 → v1 / v1 → end
이렇게 2가지 방법을 수행
'''

import heapq
import sys

input = sys.stdin.readline
N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = 1e9

for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())
def dijksta(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dis,node = heapq.heappop(q)
        if distance[node] < dis:
            continue
        for next in graph[node]:
            cost = dis + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
    return distance

original_distance = dijksta(1)
v1_distance = dijksta(v1)
v2_distance = dijksta(v2)

v1v2_path = original_distance[v1] + v1_distance[v2] + v2_distance[N]
v2v1_path = original_distance[v2] + v2_distance[v1] + v1_distance[N]

result = min(v1v2_path,v2v1_path)
print(result if result< INF else -1)