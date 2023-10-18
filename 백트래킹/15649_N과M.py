# 15649 N과N S3
# 백트래킹 중복 허용 순열
def dfs(n,lst):
    if n==m:
        ans.append(lst)
        return
    for j in range(1,N+1): 
        if visited[j] == 0:
            visited[j] =1
            dfs(n+1,lst+[j])
            visited[j]=0

N,m = map(int,input().split())
ans = []
visited = [0]*(N+1)


dfs(0,[])
for lst in ans:
    print(*lst)

