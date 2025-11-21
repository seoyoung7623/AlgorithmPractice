T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
from collections import deque
from collections import defaultdict

for test_case in range(1, T + 1):
    N,S = map(int,input().split())
    arr = list(map(int,input().split()))
    lst = [(arr[i],arr[i+1]) for i in range(0,N,2)]
    
    dic = defaultdict(set)
    for a,b in lst:
        dic[a].add(b)
    #print(dic)
    visited = [0] * 101
    
        
    
    def bfs(start):
        q = deque([start])
        visited[start] = 1
        while q:
            x = q.popleft()
            #print(x)
            for nx in dic[x]:
                #print(nx)
                if visited[nx] == 0:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
    bfs(S)    
    max_depth = max(visited)
    answer = [i for i in range(len(visited)) if visited[i] == max_depth]
    print(f"#{test_case} {max(answer)}")
    
    

