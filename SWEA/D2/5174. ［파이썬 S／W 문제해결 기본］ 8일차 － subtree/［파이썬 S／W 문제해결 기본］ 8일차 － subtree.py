T = int(input())

for test_case in range(1, T + 1):
    E,N = map(int,input().split())
    graph = [[] for _ in range(E+2)]
    arr = list(map(int,input().split()))
    lst = [(arr[i],arr[i+1]) for i in range(0,len(arr),2)]
    
    for p,c in lst:
        graph[p].append(c)
    answer = 1
    
    def dfs(x):
        global answer
        for n in graph[x]:
            answer += 1
            dfs(n)
    dfs(N)
    print(f"#{test_case} {answer}")
        
        
    