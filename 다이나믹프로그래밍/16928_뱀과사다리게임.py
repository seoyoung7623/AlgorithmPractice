# 16928 뱀과사다리게임 G5

from collections import deque


N,M = map(int,input().split())
graph = [i for i in range(101)] #인덱스 현재 위치를 저장!
visited = [0] * 101
for _ in range(N+M):
    x,y = map(int,input().split())
    graph[x] = y #이동하는 곳의 인덱스 저장

def BFS(v):
    q = deque([v])
    visited[v] = 1

    while q:
        p = q.popleft() #현재인덱스

        for i in range(1,7):
            dice = p + i # 주사위
            if dice > 100:
                continue
            cnt = graph[dice] #주사위로 이동한 인덱스
            if visited[cnt] == 0: # 방문하지않았다면
                visited[cnt] = visited[p] + 1
                q.append(cnt)

                if cnt == 100:
                    return

BFS(1)

print(visited[100]-1)


