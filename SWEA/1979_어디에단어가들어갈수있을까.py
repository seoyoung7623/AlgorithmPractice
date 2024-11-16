# 1979 어디에 단어가 들어갈 수 있을까? D2
'''
단어 시작기준
0의 4방향 탐색
벽에서 부터 시작
단어는 상 -> 하 , 좌 -> 우 방향으로만 가능하다.
가로 세로 탐색
'''

T = int(input())
for test_case in range(1,T+1):
    N,K = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        length = 0
        for j in range(N):
            if grid[i][j] == 1:
                length += 1
            else:
                if length == K:
                    ans += 1
                length = 0
        if length == K:
            ans += 1

    for i in range(N):
        length = 0
        for j in range(N):
            if grid[j][i] == 1:
                length += 1
            else:
                if length == K:
                    ans += 1
                length = 0
        if length == K:
            ans += 1
    print(f"#{test_case} {ans}")



