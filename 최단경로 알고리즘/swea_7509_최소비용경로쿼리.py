# SWEA 최소비용경로쿼리
import heapq
INF = int(1e9)

T = int(input())
def min_cost_path(H,W,gird, queries):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    total = 0
    for sx,sy,ex,ey in queries:
        sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1
        dist = [[INF] * W for _ in range(H)]
        dist[sx][sy] = grid[sx][sy]
        q = [(gird[sx][sy],sx,sy)]
        while q:
            cost,x,y = heapq.heappop(q)
            if cost > dist[x][y]:
                continue
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<H and 0<=ny<W:
                    new_cost = cost+grid[nx][ny]
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(q,(new_cost,nx,ny))
        total += dist[ex][ey]
    return total
        
    

for test_case in range(1, T + 1):
    H,W,Q = map(int,input().split())
    grid = []
    for i in range(H):
        grid.append(list(map(int,input().split())))
    queries = []
    for i in range(Q):
        queries.append(list(map(int,input().split())))
    total = min_cost_path(H,W,grid,queries)
    print(f"#{test_case} {total}")