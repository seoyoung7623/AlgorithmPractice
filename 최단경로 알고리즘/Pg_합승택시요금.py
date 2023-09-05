# Programmers 합승 택시 요금
# 다익스트라 알고리즘
import heapq
def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    for x,y,z in fares:
        graph[x].append((y,z))
        graph[y].append((x,z))
        
    def dijkstra(start):
        q = []
        lst = [INF for _ in range(n+1)]
        lst[start] = 0 # 초기화!!
        heapq.heappush(q,(0,start)) # 시작 노드 초기화 -> 첫번째 원소 길이 (0)을 기준으로 우선순위 정렬
        while q:
            dist,node=heapq.heappop(q)
            for fu,fw in graph[node]: #fu: 도착노드 ,fw: 간선
                if lst[fu] > dist + fw:
                    lst[fu] = dist + fw
                    heapq.heappush(q,(lst[fu],fu))      
        return lst # 각 노드에서 나타난 모든 노드의 경로 리스트
    distance = [[]]
    answer = INF
    for i in range(1,n+1):
        distance.append(dijkstra(i)) #각 노드에서 나타난 모든 경로 리스트
    for i in range(1,n+1):
        answer = min(answer,distance[s][i]+distance[i][a]+distance[i][b])
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))