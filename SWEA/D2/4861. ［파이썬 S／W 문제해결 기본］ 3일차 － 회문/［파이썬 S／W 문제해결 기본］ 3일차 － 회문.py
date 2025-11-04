'''
N,M
M의 길이의 회문찾기 가로, 세로
회문 확인법 +M 같은 문자면 계속 +(M-1)
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    grid = [list(input().strip()) for _ in range(N)]
    valid = False
    
    def check(arr):
        lg = len(arr)
        for k in range(lg//2):
            if arr[k] != arr[lg-k-1]:
                return False
        else:
            return True
                    
    for i in range(N):
        for j in range(N):
            if j <= N-M:
                if grid[i][j] == grid[i][j+M-1]:
                    if check(grid[i][j:j+M]):
                        print(f"#{test_case} {''.join(grid[i][j:j+M])}")
                        valid = True
  	
    for i in range(N):
        for j in range(N):
            if j <= N-M:
                if grid[j][i] == grid[j+M-1][i]:
                    row = [grid[j+x][i] for x in range(M)]
                    if check(row):
                        print(f"#{test_case} {''.join(row)}")
                        valid = True
 	
                
        
    