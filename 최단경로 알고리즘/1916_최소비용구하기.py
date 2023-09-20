# 1916 최소 비용구하기 G5
import heapq
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = 1e8
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
start,end = map(int,input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 힙큐는 첫번째 인덱스를 오름차순하기 때문에 거리가 앞에 와야함
    distance[start] = 0
    while q:
        dis, node = heapq.heappop(q)

        if distance[node] < dis: # 중복을 피하기 위한 조건 : 이미 더 짧은 경로로 방문한 적이 있음
            continue

        for next in graph[node]:
            cost = next[1] + dis
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))

dijkstra(start)
print(distance[end])
# 시간 초과?
