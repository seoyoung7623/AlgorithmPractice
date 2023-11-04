# 13549 숨바꼭질 3 G5
import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
visited = [-1 for _ in range(100001)] # 0으로 하면 x2로 갱신되었을때 방문기록을 확인 할 수 없음!
def BFS(n):
    visited[n] = 0
    q = deque([n])
    while q:
        n = q.popleft()
        if n == K:
            print(visited[n])
            return
        
        if n*2 < 100001 and visited[n*2] == -1:
            visited[n*2] = visited[n]
            q.appendleft(n*2) # n*2가 다른 연산보다 높은 우선순위를 가지기 위함

        for i in (n-1,n+1):
            if 0 <= i < 100001 and visited[i] == -1:
                visited[i] = visited[n] + 1
                q.append(i)

BFS(N)
