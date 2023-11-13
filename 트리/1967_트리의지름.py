# 1967 트리의 지름 G4
'''
1. 트리에서 아무 노드나 잡고 그 노드에 대한 가장 먼 노드를 구하고 이 노드를 n1이라고 하자.
2. n1 에대한 가장 먼 노드를 한번 더 구한다. 이 노드를 n2라고 하자.
3. 이제 n1과 n2의 거리가 트리의 지름이 된다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]

def dfs(x,wei):
    for i in graph[x]:
        a,b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a,wei+b)

# 트리구현
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

distance = [-1] * (n+1)
distance[1] = 0
dfs(1,0)

start = distance.index(max(distance))
distance = [-1] * (n+1) #길이 초기화
distance[start] = 0
dfs(start,0)

print(max(distance))

