# 1954_달팽이 숫자
'''
달팽이 숫자
N이 주어지면 (0,0)에서 시작하여 숫자를 출력한다.
1. 그래프를 채워가면서 그린다.-> 시간초과 가능성?
    종료조건: 방향을 전환했는데 한칸이라도 이동하지 못하는 경우, 마지막숫자가 N*N인 경우
시간복잡도 N*N 칸을 모두 방문하므로 O(N^2)
2. 재귀를 이용해 방향을 바꾼다.
'''
# MY
T = int(input())
diractions = [(0,1),(1,0),(0,-1),(-1,0)]
for test_case in range(1, T + 1):
    N = int(input())
    grid = [[0]*N for _ in range(N)]
    x,y = 0,0
    grid[x][y] = 1
    toggle = False
    while True:
        for dx,dy in diractions:
            if 0<=x+dx<N and 0<=y+dy<N and grid[x+dx][y+dy]==0:
                while True:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<N and grid[nx][ny]==0:
                        grid[nx][ny] = grid[x][y] + 1
                        x, y = nx, ny
                    else:
                        break
            else:
                toggle = True
                break

        if toggle:
            break
    print(f"#{test_case}")
    for n in range(N):
        print(*grid[n])

# 재귀
T = int(input())
diractions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for test_case in range(1, T + 1):
    N = int(input())
    grid = [[0] * N for _ in range(N)]
    def snail(x,y,d,num):
        grid[x][y] = num
        if num == N*N:
            return
        nx = x + diractions[d][0]
        ny = y + diractions[d][1]
        if 0<=nx<N and 0<=ny<N and grid[nx][ny] == 0:
            snail(nx,ny,d,num+1)
        else:
            snail(x,y,(d+1)%4,num)

    snail(0,0,0,1)
    print(f"#{test_case}")
    for n in range(N):
        print(*grid[n])



