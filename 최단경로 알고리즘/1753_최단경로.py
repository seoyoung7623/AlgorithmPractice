# 1753 최단경로 G4
import heapq
import sys
input = sys.stdin.readline
V,E = map(int,input().split())
K = int(input())
INF = int(1e9)
distance = [INF] * (V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dis,node = heapq.heappop(q)
        for next in graph[node]:
            cost = next[1] + distance[node]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
dijkstra(K)
for i in range(1,len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
