from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for e in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    S,G = map(int,input().split())
    visited = [0]*(V+1)
                
    def bfs(x):
        q = deque([x])
        while q:
            x = q.popleft()
            for n in graph[x]:
                if visited[n] == 0:
                    visited[n] = visited[x] + 1
                    if n == G:
                        return visited[n]
                    q.append(n)
        return 0
    
        
    
    print(f"#{test_case} {bfs(S)}")
    
            