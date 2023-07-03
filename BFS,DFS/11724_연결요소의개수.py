# 11724 연결요소의 개수
'''
- 깊이우선
- 너비우선
기존에 공부한 DFS, BFS 참고함
'''
import sys
sys.setrecursionlimit(5000) # 재귀 함수 호출을 위한 Python 인터프리터 스택의 최대 깊이를 늘림. 기본은 1000
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)] # 2차원리스트 빈 리스트로 선언 가능
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False]*(N+1)
cnt = 0

def DFS(v,depth):
    visited[v] = True

    for j in graph[v]:
        if not visited[j]:
            DFS(j,depth+1)

for i in range(1,N+1):
    if visited[i] == False:
        if not graph[i]:
            cnt+=1
            visited[i] = True
        else:
            DFS(i,0)
            cnt+=1
print(cnt)
