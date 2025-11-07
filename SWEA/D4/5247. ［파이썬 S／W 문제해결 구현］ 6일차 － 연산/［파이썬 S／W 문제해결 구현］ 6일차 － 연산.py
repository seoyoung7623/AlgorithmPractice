from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    answer = []
    visited = set()
    
    def BFS(start):
        q = deque([(0,start)])
        visited.add(start)
        maximum = int(1e6)
        while q:
            cnt, x = q.popleft()
            if x == M:
                return cnt
            for nx in (x+1,x-1,x*2,x-10):
                if nx not in visited and nx <= maximum and nx > 0:
                    q.append((cnt+1,nx))
                    visited.add(nx)
                    
    print(f"#{test_case} {BFS(N)}")

        
    
        
    