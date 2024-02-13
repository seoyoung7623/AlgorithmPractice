# 프림알고리즘
'''
시작정점에서 출발하여 정점을 하나씩 선택해 신장트리 집합을 확장해나감
'''
import heapq
n,m = map(int,input().split())
graph = list([] for _ in range(n))
visited = [0] *(n+1)

for i in range(m):
    u,v,weight = map(int,input().split())
    graph[u].append([weight,u,v])
    graph[v].append([weight,v,u])

def prim(graph,start_node):
    visited[start_node] = 1
    candidate = graph[start_node]
    heapq.heapify(candidate) #우선순위 큐 생성
    mst = []
    total_weight = 0 # 전체 가중치

    while candidate:
        # 간선 추출
        weight,u,v = heapq.heappop(candidate) #가중치가 가장 작은 간선 추출
        # 간선을 방문 하지 않았다면, 가중치를 추가, 그 간선에서 인접 간선의 방문여부 판단
        # 방문하지 않았다면 우선순위큐에 삽입
        if visited[v] == 0: # 우선순위큐는 가중치가 작은 값이 먼저 나오므로 이미 들어와있는것중 방문표시가 되어있는것이 있을 수 있음!
            # 이 부분이 사이클을 막아줌
            visited[v] = 1
            mst.append((u,v))
            total_weight += weight

            for edge in graph[v]: # 다음 인접 간선탐색
                if visited[edge[2]] == 0: # 방문한 노드가 아니라면 힙에 추가
                    heapq.heappush(candidate,edge)
    return total_weight
