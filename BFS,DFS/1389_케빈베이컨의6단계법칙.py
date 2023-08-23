# 1389 케빈베이컨의 6단계법칙 S1
from collections import deque


N,M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(M)]
resultLst = []

def BFS(i):
    queue = deque()
    visited = [False]*(N+1)
    result = [0]*(N+1)
    queue.append(i)
    visited[i] = True

    while queue:
        num = queue.popleft()
        for n in range(len(lst)):
            if lst[n][0] == num and visited[lst[n][1]] == False:
                visited[lst[n][1]] = True
                result[lst[n][1]] = result[lst[n][0]]+1
                queue.append(lst[n][1])
            if lst[n][1] == num and visited[lst[n][0]] == False:
                visited[lst[n][0]] = True
                result[lst[n][0]] = result[lst[n][1]]+1
                queue.append(lst[n][0])
    resultLst.append(sum(result))

for i in range(1,N+1):
    BFS(i)
print((resultLst.index(min(resultLst))+1))