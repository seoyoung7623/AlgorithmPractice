'''
백트래킹
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    answer = int(1e9)
    visited = []
    
    def dfs(row,total):
        global answer, visited
        if total > answer:
            return
        if row == N:
            #print(total)
            answer = min(answer, total)
            return
        for i in range(N):
            if i not in visited:
                visited.append(i)
                dfs(row+1,total +  graph[row][i])
                visited.pop()
                
    dfs(0,0)
    print(f"#{test_case} {answer}")
    
        