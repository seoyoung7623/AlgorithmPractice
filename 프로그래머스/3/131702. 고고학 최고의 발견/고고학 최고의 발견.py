import copy
from itertools import product

def solution(clockHands):
    INF = 1e9
    answer = INF
    length = len(clockHands)

    def turn(x,y,grid,k): # k는 돌리는 횟수
        rotation = ((x,y),(x-1,y),(x+1,y),(x,y-1),(x,y+1))
        for r in rotation:
            nx,ny = r
            if 0<=nx<length and 0<=ny<length:
                grid[nx][ny] = (grid[nx][ny] + k) % 4

    for first_ops in product(range(4),repeat=length):
        grid = copy.deepcopy(clockHands)
        move = 0
        for c,k in enumerate(first_ops):
            if k:
                move += k
                turn(0,c,grid,k)
        possiable = True
        for i in range(1,length):
            for j in range(length):
                if grid[i-1][j] != 0:
                    cnt = (4 - grid[i-1][j]) % 4
                    turn(i, j, grid, cnt)
                    move += cnt   
            if move >= answer:
                possiable = False
                break
        if not possiable:
            continue

        if all(x == 0 for x in grid[length-1]):
            answer = min(answer,move)
    return 0 if answer == INF else answer

print(solution([[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]))