# # 15683 감시 G3
# '''
# 내코드: 백트래킹접근으로 1~5까지 경우 나눠서 계산
# '''
# from collections import deque
# from itertools import combinations
# import sys,copy

# N,M = map(int,input().split())
# grid = [list(map(int,input().split())) for _ in range(N)]
# cctvs = []
# for i in range(N):
#     for j in range(M):
#         if grid[i][j] !=0 and grid[i][j] != 6:
#             cctvs.append((i,j))
# answer = 1e9

# def total(grid):
#     sum = 0
#     for i in range(N):
#         for j in range(M):
#             if grid[i][j] == 0:
#                 sum += 1
#     return sum
# def backtracking(grid,c):
#     global answer
#     if c == len(cctvs):
#         answer = min(total(grid),answer)
#         return
#     for i in range(c,len(cctvs)):
#         x,y = cctvs[i]
#         directions = [(1,0),(0,1),(-1,0),(0,-1)]
#         if grid[x][y] == 1:
#             for dx,dy in directions:
#                 x,y = cctvs[i]
#                 grid_copy  = copy.deepcopy(grid)
#                 while 1:
#                     x = x + dx
#                     y = y + dy
#                     if 0<=x<N and 0<=y<M and grid[x][y] != 6:
#                         grid_copy[x][y] = '#'
#                     else:
#                         break
#                 backtracking(grid_copy,c+1)
#         elif grid[x][y] == 2:
#             grid_copy  = copy.deepcopy(grid)
#             for dx,dy in [directions[0],directions[2]]:
#                 x,y = cctvs[i]
#                 while 1:
#                     x += dx
#                     y += dy
#                     if 0<=x<N and 0<=y<M and grid[x][y] != 6:
#                         grid_copy[x][y] = '#'
#                     else:
#                         break
#             backtracking(grid_copy,c+1)
#             grid_copy  = copy.deepcopy(grid)
#             for dx,dy in [directions[1],directions[3]]:
#                  x,y = cctvs[i]
#                  while 1:
#                     x += dx
#                     y += dy
#                     if 0<=x<N and 0<=y<M and grid[x][y] != 6:
#                         grid_copy[x][y] = '#'
#                     else:
#                         break
#             backtracking(grid_copy,c+1)
#         elif grid[x][y] == 3:
#             for com in combinations(cctvs,3):
#                 grid_copy  = copy.deepcopy(grid)
#                 for dx,dy in com:
#                     x,y = cctvs[i]
#                     while 1:
#                         x += dx
#                         y += dy
#                         if 0<=x<N and 0<=y<M and grid[x][y] != 6:
#                             grid_copy[x][y] = '#'
#                         else:
#                             break
#                 backtracking(grid_copy,c+1)
#         elif grid[x][y] == 4:
#             grid_copy  = copy.deepcopy(grid)
#             for dx,dy in directions:
#                 x,y = cctvs[i]
#                 while 1:
#                     x = x + dx
#                     y = y + dy
#                     if 0<=x<N and 0<=y<M and grid[x][y] != 6:
#                         grid_copy[x][y] = '#'
#                     else:
#                         break
#             backtracking(grid_copy,c+1)


# backtracking(grid,0)
# print(answer)

'''
참고 코드
백트래킹이용 dfs 로직
접근 방법은 같았으나 구현이 어려웠음
'''
import copy

# 방향 정의 (우, 하, 좌, 상)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# CCTV별 가능한 방향 설정!! 한번에 마크하기 위해서
cctv_directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}

# 맵의 크기 및 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# CCTV 위치 저장
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= grid[i][j] <= 5:
            cctvs.append((i, j, grid[i][j]))

# 감시 영역을 표시
def mark(grid, x, y, direction):
    nx, ny = x + directions[direction][0], y + directions[direction][1]
    while 0 <= nx < N and 0 <= ny < M: # 범위를 벗어나면 종료
        if grid[nx][ny] == 6:  # 벽에 부딪히면 종료
            break
        if grid[nx][ny] == 0:  # 감시 가능 영역 표시
            grid[nx][ny] = '#'
        nx += directions[direction][0] #계속 1씩 증가
        ny += directions[direction][1] #계속 1씩 증가

# 백트래킹 탐색
def dfs(depth, grid):
    if depth == len(cctvs):  # 모든 CCTV 처리 완료
        return sum(row.count(0) for row in grid)  # 사각지대 계산

    x, y, type_ = cctvs[depth] #행,열,번호
    min_blind = float('inf')

    for dirs in cctv_directions[type_]:
        # 맵 복사
        new_grid = copy.deepcopy(grid)
        for d in dirs:
            mark(new_grid, x, y, d)
        # 다음 CCTV 처리
        min_blind = min(min_blind, dfs(depth + 1, new_grid))
    
    return min_blind

# 결과 출력
result = dfs(0, grid)
print(result)
