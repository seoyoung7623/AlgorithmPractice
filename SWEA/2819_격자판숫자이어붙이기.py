# 격자판에 숫자 이어붙이기 D4
# DFS

from collections import deque

T = int(input())
diractions = [[1,0],[0,1],[-1,0],[0,-1]]
def DFS(x,y,string,depth,numSet):
    if depth == 7:
        numSet.add(string)
        return
    for dx,dy in diractions:
        nx = x + dx
        ny = y + dy
        if 0<=nx<4 and 0<=ny<4:
            DFS(nx,ny,string+grid[nx][ny],depth+1,numSet)    
    return numSet

for test_case in range(1, T + 1):
    grid = []
    for _ in range(4):
        grid.append(list(map(str,input().split())))
    numSet = set()
    for i in range(4):
        for j in range(4):
            string = grid[i][j]
            numSet |= DFS(i,j,grid[i][j],1,numSet)
    print(f"#{test_case} {len(numSet)}")  