N,M = map(int,input().split())

ice = [list(map(int,input())) for _ in range(N)]
cnt = 0

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
    
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            cnt +=1
print(cnt)

