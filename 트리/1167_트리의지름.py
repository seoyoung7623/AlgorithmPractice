# 1167 트리의 지름 G2
'''
재귀 깊이를 늘려주어 런타임 에러를 해결한다.
백준의 기본 재귀 깊이는 10^3 밖에 안됨 따라서 N의 최대는 10^5이므로
10^6으로 늘려주었음.
'''
import sys
sys.setrecursionlimit(10**6)

v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    pairs = list(map(int,input().split()[:-1])) # 맨마지막 -1를 제외한 숫자들을 리스트로 가져옴
    for i in range(1,len(pairs),2):
        graph[pairs[0]].append((pairs[i],pairs[i+1]))

def DFS(x,wei): # 다음 트리, 경로값
    for i in graph[x]:
        a,b = i
        if distance[a] == -1:
            distance[a] = wei + b
            DFS(a,wei+b)


    
distance = [-1] * (v+1)
distance[1] = 0
DFS(1,0)

idx = distance.index(max(distance))
distance = [-1] * (v+1)
distance[idx] = 0
DFS(idx,0)

print(max(distance))

