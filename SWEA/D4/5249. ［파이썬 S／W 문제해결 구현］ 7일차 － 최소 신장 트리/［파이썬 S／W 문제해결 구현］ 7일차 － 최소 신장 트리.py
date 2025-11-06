import heapq

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    
    for e in range(E):
        n1,n2,w = map(int,input().split())
        graph[n1].append((n2,w))
        graph[n2].append((n1,w))

    hq = [(0,0)]
    visited = [False] * (V+1)
    answer = 0
    
    while hq:
        w, n = heapq.heappop(hq)
        if visited[n]:
            continue
        visited[n] = True
        answer += w
        if False not in visited:
            break
        for next_node, cost in graph[n]:
            if visited[next_node] == False:
                heapq.heappush(hq,(cost,next_node))
    print(f"#{test_case} {answer}")
    