#11725 트리의 부모 S2
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
result = [0]*(N+1)
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def BFS():
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                result[i] = node

BFS()
for i in range(2,N+1):
    print(result[i])
