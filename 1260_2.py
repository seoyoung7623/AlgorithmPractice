#1260 dfs bfs 내가 다시 짠 코드
#아직 안됨;

from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visit_list1[v] = 1
    while q:
        v = q.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if visit_list1[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list1[i] = 1

def dfs(v):
    print(v,end=' ')
    visit_list2[v] = 1
    for i in range(1,n+1):
        if visit_list1[i] == 0 and graph[v][i] == 1:
            dfs(i)

n,m,v = map(int,input().split())
#모든접선을 확인하는 graph
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visit_list1 = [0]*(n+1)
visit_list2 = [0]*(n+1)

dfs(v)
print()
bfs(v)


    