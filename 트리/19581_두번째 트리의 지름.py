# 19581 두번째 트리의 지름 G1
'''
임의의 지점에서 가장 먼 지점 A / A에서 두번째로 먼 지점 B
임의의 지점에서 두번짹로 가장 먼 지점 C / C에서 가장 먼 지점 D
https://dlwnsdud205.tistory.com/86 c++언어 파이썬으로 해석
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
distance1 = [-1] * (N+1)
distance2 = [-1] * (N+1)
visited = [0] * (N+1) 
for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def DFS(x,wei,distance1,distance2):
    for i in graph[x]:
        b,c = i
        if distance1[b] == -1:
            distance1[b] = max(distance2[b],c+wei)
            DFS(b,c + wei,distance1,distance2)

distance1[1] = 0
DFS(1,0,distance1,distance2)

# 임의의 지점에서 가장 먼 지점 A / A에서 두번째로 먼 지점 B
firstIdx = distance1.index(max(distance1))
distance1[firstIdx] = -1

distance2[firstIdx] = 0
DFS(firstIdx,0,distance2,distance1)
large = max(distance2)
distance2.remove(max(distance2))
result = []
result.append(max(distance2))

# 임의의 지점에서 두번짹로 가장 먼 지점 C / C에서 가장 먼 지점 D
distance2 = [-1] * (N+1)
secondIdx = distance1.index(max(distance1))
distance2[secondIdx] = 0
DFS(secondIdx,0,distance2,distance1)

# 예제 2번과 같이 두가지 경우의 거리가 같은 경우 2번 경우의 두번째 지점을 비교하게 한다.
if max(distance2) == large:
    distance2[distance2.index(max(distance2))] = -1
result.append(max(distance2))

# 두가지 경우중에 가장 큰 거리
print(max(result))
