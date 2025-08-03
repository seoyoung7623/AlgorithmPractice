#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1707                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1707                           #+#        #+#      #+#     #
#    Solved: 2025/06/05 10:22:40 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
3 2
1 - 3
2 - 3

4 4
1 - 2
2 - 3
3 - 4
4 - 2

각 정점이 다른 색이면 이분 그래프
BFS
어느정점에서 시작해도 상관없음

3개의 정점
1-3
2-3
1-2 가 있으면 이분 그래프가 아님 
다음 노드가 같은 색과 연결되면 안됨
'''

# import sys
# from collections import deque
# K = int(input())
# input = sys.stdin.readline

# def bfs(start):
#     toggle = False
#     q = deque([start])
#     colors = [0]*(V+1)
#     color = -1
#     colors[start] = color
#     while q:
#         x = q.popleft()
#         for k in graph[x]:
#             if colors[k] == color:
#                 toggle = True
#                 break
#             elif colors[k] == 0:
#                 colors[k] = -color
#                 color = -color
#                 q.append(k)
#         if toggle:
#             break
#     return toggle

# for test_case in range(K):
#     V,E = map(int,input().split()) # 정점의 개수, 간선의 개수
#     graph = [[] for _ in range(V+1)]
#     for i in range(E):
#         u,v = map(int,input().split())
#         graph[u].append(v)
#         graph[v].append(u)

#     if bfs(1):
#         print('NO')
#     else:
#         print('YES')

'''
BFS는 첫노드만 하면 안됨
사이클을 대처할 수 없음. 따라서 모든 정점에 대해 방문하지 않은 경우 BFS 실행을 해야한다.
'''
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
