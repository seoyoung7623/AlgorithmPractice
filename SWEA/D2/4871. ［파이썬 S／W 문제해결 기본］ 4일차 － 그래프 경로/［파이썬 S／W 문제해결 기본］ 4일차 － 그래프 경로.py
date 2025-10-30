'''
group 노드 경로
visited 이용
'''

T = int(input())

for test_case in range(1, T + 1):
    V,E = map(int,input().split())
    group = [[] for _ in range(V+1)]
    
    for e in range(E):
        a,b = map(int,input().split())
        group[a].append(b)
    S,G = map(int,input().split())
    visited = [0]*(V+1)
    visited[S] = 1
    
    def dfs(x):
        if x == G:
            return True
        visited[x] = 1
        for n in group[x]:
            if visited[n] == 0:
                if dfs(n):
                    return True
        return False
    
    if dfs(S):
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
            
            
            
        
    