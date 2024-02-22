# Programmers 합승 택시 요금
# 1.다익스트라 알고리즘
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

# 2.플로이드 와샬 알고리즘
def solution2(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[INF] * (n+1) for _ in range(n+1)] # 2중 리스트 생성

    def floyd_warshall():
        for k in range(1,1+n):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if i == j:
                        graph[i][j] = 0 # 대각선 0으로 초기화
                    else:
                        graph[i][j] = min(graph[i][k] + graph[k][j],graph[i][j])

    for x,y,z in fares:
        graph[x][y] = z
        graph[y][x] = z
    floyd_warshall()

    for i in range(1,n+1):
        answer = min(graph[s][i]+graph[i][a]+graph[i][b],answer)
    return answer
print(solution2(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


# 2024.02.22 다시 풀었으나 코드를 참고함
import heapq

INF = int(1e9)

def dijkstra(start,end):
    global graph
    n = len(graph)
    heap = [(0,start)]
    dist = [INF] * (n+1)
    dist[start] = 0 # 첫점 0으로 지정해서 탐색완료 표시
    while heap:
        w,u = heapq.heappop(heap)
        
        # 거리값이 크면 갱신하지 않음
        if dist[u]<w:
            continue
            
        for node in graph[u]:
            cost = w + node[0]
            if cost < dist[node[1]]:
                dist[node[1]] = cost
                heapq.heappush(heap,(cost,node[1])) 
    return dist[end]
                

def solution(n, s, a, b, fares):
    global graph
    graph = [[] for _ in range(n+1)]
    for u,v,w in fares:
        graph[u].append((w,v))
        graph[v].append((w,u)) 

    cost = dijkstra(s,a) + dijkstra(s,b)
    for i in range(1,n+1):  
        if s != i:
            cost = min(cost,dijkstra(s,i)+dijkstra(i,a)+ dijkstra(i,b))
    return cost
print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))