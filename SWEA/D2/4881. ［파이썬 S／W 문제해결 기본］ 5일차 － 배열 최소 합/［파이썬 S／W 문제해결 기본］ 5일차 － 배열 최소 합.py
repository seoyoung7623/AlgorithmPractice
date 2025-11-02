T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * (N)
    answer = 1e5
    
    def dfs(r,cnt):
        global answer
        if cnt >= answer:
            return
        if r ==N:
            answer = min(answer,cnt)
            return
        
        for c in sorted(range(N), key=lambda x: grid[r][x]):
            if visited[c] == False:
                visited[c] = True
                dfs(r+1,cnt + grid[r][c])
                visited[c] = False

            
    dfs(0,0)
    print(f"#{test_case} {answer}")