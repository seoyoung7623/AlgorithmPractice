'''
최소 경로 거리
다익스트라 알고리즘 
이동 배열을 inf로 초기화하고 짧은 경로로 갱신
inf,1,
'''
import heapq
T = int(input())

for test_case in range(1, T + 1):
    INF = int(1e9)  # 정수로 변경
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    
    # 변수명 충돌 해결
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
 
    def dijkstra1(start):
        distances = [INF] * (N+1)
        distances[start] = 0
        hq = [(0, start)]
        
        while hq:
            d, node = heapq.heappop(hq)
            
            if d > distances[node]:
                continue
            # print(distances)
            for next_node, w in graph[node]:
                new_cost = d + w
                if new_cost < distances[next_node]:
                    distances[next_node] = new_cost
                    heapq.heappush(hq, (new_cost, next_node))
        
        return distances
    
    dist = dijkstra1(0)
    
    # 도달 불가능한 경우 처리
    result = dist[N] if dist[N] != INF else -1
    print(f"#{test_case} {result}")