# 1249 보급로 D4
import heapq
T = int(input())
INF = int(1e9)
directions = [[1,0],[0,1],[-1,0],[0,-1]]

for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input())))
    distance = [[INF]*N for _ in range(N)]
    distance[0][0] = 0
    q = [(0,0,0)] 
    while q:
        cost,x,y = heapq.heappop(q)
        if cost > distance[x][y]:
            continue
        for dx,dy in directions:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                if cost + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = cost + graph[nx][ny]
                    heapq.heappush(q,(distance[nx][ny],nx,ny))
    print(f'#{test_case} {distance[N-1][N-1]}')
