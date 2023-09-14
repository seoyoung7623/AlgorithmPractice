import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split()) # 노드 수, 간선 수
start = int(input()) # 시작 노드
INF = int(1e9)
distance = [INF] * (n+1) # 총 거리
graph = [[] for _ in range(n+1)]
for _ in range(m): #a번 노드에서 b번노드로 가는 비용이 c
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) #

# heapq 오름차순으로 힙정렬 수행됨
def dijkstra(start):  
    q =[]
    heapq.heappush(q,(0,start)) # 빈 q, 시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0 #시작노드 기록
    while q:
        dist,node = heapq.heappop(q) #큐에서 꺼냄 길이와, 노드
        if distance[node] < dist: #큐에서 뽑아낸 거리가 이미 갱신 된 거리보다 클경우 무시
             continue
        for next in graph[node]: #큐에서 뽑아낸 노드와 인접된 인접노드들 탐색
            cost = distance[node] + next[1] # 시작 -> node + node->node의 인접 노드
            if cost < distance[next[0]]: #cost < 시작 -> 노드의 인접노드 거리 바뀐값만 힙에 넣어줌 
                # 새로운 간선이 더 작은 경우 갱신
                distance[next[0]] = cost #cost로 초기화
                heapq.heappush(q,(cost,next[0])) # dist에 바뀐값과, 도착노드를 넣어줌

dijkstra(start)

for i in range(1,len(distance)):
    if distance[i] == INF:
        print("도달할 수 없음")
    else:
        print(distance[i])

