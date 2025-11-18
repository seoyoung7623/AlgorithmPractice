from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,E,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for e in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)

    def dfs(x,colors):
        if x > N:
            return True
        for i in range(1,M+1):
            # 인접 정점에 같은 색이 있는지 검사 이전 값 검사
            ok = True
            for nx in graph[x]:
                if colors[nx] == i:
                    ok = False
                    break
            if not ok:
                continue
            
            # 색칠해보고 다음정점으로 이동
            colors[x] = i
            if dfs(x+1,colors):
                return True
            colors[x] = 0
            
        return False
                
    colors = [0] * (N+1)   
    result = 1 if dfs(1,colors) else 0
    print(f"#{test_case} {result}")
    
                
        