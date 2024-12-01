# 17070 파이프 옮기기 G5
'''
3차원배열로 dp구현
벽은 어떻게?
    대각선 파이프: 현재노드가 벽이거나 위, 왼쪽이 벽인 경우도 대각선파이프 불가능
'''
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)] # 3차원배열

def solution():
    '''
    그래프의 첫 행은 파이피가 올 수 없음!
    가로로 시작하기 때문에 1열의 가로는 모두 1이다.
    '''
    dp[0][0][1] = 1
    for i in range(2,N):
        if board[0][i] == 0: # 벽이 아닌 경우
            dp[0][0][i] = dp[0][0][i-1]
    
    for r in range(1,N):
        for c in range(1,N):
            # 대각선 파이프 처리
            # 벽에는 파이프가 올수 없음 and 벽 다음에는 파이프가 올 수 없음
            if board[r][c] == 0 and board[r-1][c] == 0 and board[r][c-1] == 0:
                dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
            
            if board[r][c] == 0:
                # 가로 파이프
                dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
                # 세로 파이프
                dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
    print(sum(dp[i][N-1][N-1] for i in range(3)))

solution()

    
