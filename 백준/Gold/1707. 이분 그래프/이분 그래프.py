import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    colors[start] = 1  # 1 또는 -1

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if colors[neighbor] == 0:
                colors[neighbor] = -colors[node]
                q.append(neighbor)
            elif colors[neighbor] == colors[node]:
                return False  # Conflict 발생: 이분 그래프 아님
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    colors = [0] * (V+1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    is_bipartite = True
    for i in range(1, V+1):
        if colors[i] == 0:
            if not bfs(i):
                is_bipartite = False
                break

    print("YES" if is_bipartite else "NO")
