import copy

N = int(input())
grid = [list(input()) for _ in range(N)]

max_candies = 1

# 모두 검사
def count_max_candies(new_grid,n):
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(1,n): # 해당 행까지만 검사
            if new_grid[i][j] == new_grid[i][j-1]:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 1
        count = 1
        for j in range(1,n): #해당 열까지만 검사
            if new_grid[j][i] == new_grid[j-1][i]:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 1
    return max_count


# 사탕 자리 변경
for i in range(N):
    for j in range(N):
        for dx,dy in [(0,1),(1,0)]:
            nx = dx + i
            ny = dy + j
            if 0<=nx<N and 0<=ny<N:
                grid[i][j],grid[nx][ny] = grid[nx][ny],grid[i][j] # 자리 변경
                max_candies = max(count_max_candies(grid,N),max_candies)
                grid[i][j],grid[nx][ny] = grid[nx][ny],grid[i][j] # 원상 복구


print(max_candies)