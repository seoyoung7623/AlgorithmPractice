# 1238 파티 G3
import heapq
import sys
input = sys.stdin.readline

N,M,X = map(int,input().split())
INF = int(1e8)
result = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start,end):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dis,node = heapq.heappop(q)
        if distance[node] < dis:
            continue
        for next in graph[node]:
            cost = next[1] + dis
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
    return distance[end]

for i in range(1,N+1):
    if i == X:
        result[i] = 0
    else:
        result[i] += dijkstra(i,X)
        result[i] += dijkstra(X,i)
print(max(result))
    