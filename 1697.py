#1697 숨바꼭질
# from collections import deque

# N,K = map(int,input().split())
# visited = [0 for _ in range(100001)]

# queue = deque()

# def bfs(n):
#     queue.append(n)

#     while queue:
#         n = queue.popleft()
#         if n == K:
#             return visited[n]
#         for nx in (n-1,n+1,n*2):
#             if 0<= nx <= 100000 and not visited[nx]:
#                 visited[nx] = visited[n] + 1
#                 queue.append(nx)

# print(bfs(N))

from collections import deque

N,K = map(int,input().split())
visited = [0 for _ in range(100001)] #범뒤 100000범위도 포함하므로 100001

def bfs(n):
    q = deque([n])

    while q:
        n = q.popleft()

        if n == K:
            return visited[n]

        for i in (n-1,n+1,n*2):
            if 0<= i <= 100000 and not visited[i]: #if not 리스트가 비어있는지 확인 범위 100000인덱스도 포함
                visited[i] = visited[n] + 1
                q.append(i)

print(bfs(N))

