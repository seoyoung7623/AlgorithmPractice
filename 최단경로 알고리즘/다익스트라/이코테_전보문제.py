# 이코테 전보문제 
# 최단 경로 알고리즘
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N,M,C = map(int,input().split())
distance = [INF]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) #초기 값 0 으로 갱신
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))

        
cnt = 0
max_distance = 0
dijkstra(C)
for i in distance:
    if i != 1e9:
        cnt+=1
        max_distance = max(max_distance,i)
print(cnt-1,max_distance)
