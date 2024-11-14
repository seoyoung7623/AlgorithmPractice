# 정답버전
game = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # 맵 설정 및 목표 위치들 추출
    Map = [list(input()) for _ in range(n)]
    start = []
    goal = []

    for i in range(n):
        for j in range(m):
            if Map[i][j] == 'w' or Map[i][j] == 'W':
                start = [i, j]  # 플레이어의 시작 위치 저장
            if Map[i][j] in ('+', 'W', 'B'):
                goal.append([i, j])  # 목표 위치 리스트에 저장

    command = list(input())  # 명령어 리스트

    # 이동 방향 설정
    move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    x, y = start  # 플레이어 시작 좌표 설정

    # 명령어 처리
    for com in command:
        dx, dy = move[com]
        nx, ny = x + dx, y + dy  # 이동할 위치 계산

        # 빈 공간 또는 목표 지점으로 이동하는 경우
        if Map[nx][ny] == '.' or Map[nx][ny] == '+':
            Map[x][y] = '.' if [x, y] not in goal else '+'
            Map[nx][ny] = 'W' if [nx, ny] in goal else 'w'
            x, y = nx, ny

        # 박스를 밀어야 하는 경우
        elif Map[nx][ny] in ('b', 'B'):
            nnx, nny = nx + dx, ny + dy  # 박스 다음 위치 계산
            if Map[nnx][nny] == '.':
                Map[x][y] = '.' if [x, y] not in goal else '+'
                Map[nx][ny] = 'W' if [nx, ny] in goal else 'w'
                Map[nnx][nny] = 'B' if [nnx, nny] in goal else 'b'
                x, y = nx, ny

            elif Map[nnx][nny] == '+':
                Map[x][y] = '.' if [x, y] not in goal else '+'
                Map[nx][ny] = 'W' if [nx, ny] in goal else 'w'
                Map[nnx][nny] = 'B'
                x, y = nx, ny

        # 모든 목표 지점에 박스가 놓인 경우 게임 종료
        if all(Map[tx][ty] == 'B' for tx, ty in goal):
            break

    # 결과 출력
    if any(Map[tx][ty] != 'B' for tx, ty in goal):
        print(f'Game {game}: incomplete')
    else:
        print(f'Game {game}: complete')

    for row in Map:
        print("".join(row))
    game += 1
