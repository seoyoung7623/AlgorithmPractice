#1260 DFS와 BFS
# graph = dict()

# graph['1'] = '2','3'
# str = '1'
# if str in graph:
#     print(list(graph[str]).extend('4'))
#     graph[str] = list(graph[str]).append('4')
#     print(graph[str])

# def dfs(numlist,V):
#     visited = []
#     need_visited = deque()
#     need_visited.append(V)
#     while need_visited:
#         node = need_visited.pop()
#         if node not in visited:
#             visited.append(node)
#             need_visited.append(numlist)

# N, M, V = map(int,input().split())
# DFSList = []
# numlist = []
# need_visited = []
# for i in range(M):
#     numlist.append(list(map(int,input().split())))
# DFSList.append(V)

# for i in range(len(numlist)):
#     if V in numlist[i][0]:
#         need_visited.append(numlist[i][0])
#         del numlist[i][0]

from collections import deque
def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft()
        print(v,end=" ")
        for i in range(1,n+1):
            if visit_list[i] == 0 and graph[v][i] ==1:
                q.append(i)
                visit_list[i] = 1

def dfs(v):
    visit_list2[v] = 1
    print(v,end=" ")
    for i in range(1, n+1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)

n,m,v = map(int,input().split())

graph = [[0] *(n+1) for _ in range(n+1)]
visit_list = [0]*(n+1)
visit_list2 = [0]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)