# 가장 먼 노드
from collections import deque

def solution(n, edge):
    answer = 0
    result = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
 
    
    def BFS():
        q = deque([1])
        result[1] = 1
        while q:
            node = q.popleft()
            for i in graph[node]:
                if result[i] == 0:
                    result[i] = max(result[i],result[node] + 1)
                    q.append(i)
                
                
        
    BFS()   
    max_num = max(result)  
    print(result) 
        
    # BFS로 저장해 노드 리스트의 가장 큰 값을 출력한다.
    return result.count(max_num)  
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2],[5,6]]))