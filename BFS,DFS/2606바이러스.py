#2606 바이러스
'''
from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m): #그래프 생성
    x,y = list(map(int,input().split()))
    graph[x] +=[y]
    graph[y] +=[x] #양방향 그래프
visited[1] = 1
q = deque([1])
while q:
    c = q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            q.append(nx)
            visited[nx] = 1
print(sum(visited) - 1)
'''

#1. BFS방식
'''
from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)] #입력받을곳
visited = [0]*(n+1)

for i in range(m):
    x,y = list(map(int,input().split()))
    graph[x] += [y]
    graph[y] += [x]

q = deque([1])
visited[1] = 1
while q:
    s = q.popleft()
    for nx in graph[s]:
        if visited[nx] == 0:
            visited[nx] = 1
            q.append(nx)
print(sum(visited)-1)
'''

# DFS방식
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    x,y = map(int,input().split())
    graph[x] += [y]
    graph[y] += [x]

def dfs(s):
    visited[s] = 1

    for i in graph[s]:
        if visited[i] == 0:
            dfs(i)
dfs(1)
print(sum(visited) -1)

     