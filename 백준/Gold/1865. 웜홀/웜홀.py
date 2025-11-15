TC = int(input())
for tc in range(TC):
    N,M,W = map(int,input().split())
    edges = []

    for m in range(M):
        s,e,t = map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    for w in range(W):
        s,e,t = map(int,input().split())
        edges.append((s,e,-t))
    
    def bellman_ford(n,edges):
        dist = [0] * (N+1)

        # 간선 전체를 N-1만큼 돌고 (최대 간선을 N-1이기때문에)
        # 마지막에서 음수 사이클을 확인함
        for _ in range(n-1):
            for s,e,t in edges:
                if dist[e] > dist[s] + t: # 큰 값으로 갱신
                    dist[e] = dist[s] + t
        
        
        for s,e,t in edges:
            if dist[s] + t < dist[e]:
                return True
            
        return False
    
    if bellman_ford(N,edges):
        print("YES")
    else:
        print("NO")

    