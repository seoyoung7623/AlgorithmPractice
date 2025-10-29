from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    INF = 1e7
    L,M,N = map(int,input().strip().split())
    
    checking = set()
    count = [0]*(L+1)
    
    move = [N,-N,M,-M]
    
    q = deque([1])
    count[1] = 0
        
    while q:
        x = q.popleft()
        for m in move:
            nx = x+m
            if 0 < nx <= L and count[nx] == 0:
                count[nx] = count[x] + 1
                q.append(nx)
      
    print(f"#{test_case} {max(count)}")
                
                
                
        
    