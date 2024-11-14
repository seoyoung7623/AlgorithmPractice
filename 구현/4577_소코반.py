# 4577 소코반 G3
'''
w를 기준으로 알파벳 이동을 실행
종료조건: b가 모두 B가 되면 즉시 종료
    incomplete: 경로를 모두 이동했는데 b가 있는경우
    complete: b가 모두 B가 되는경우
    그 그래프를 출력해야하기 때문에 grid에 값을 저장한다.
    
이동: 1. w가 가는 방향에 b(B)가 있다면 이동
    2. w가 가는 방향, b가 가는 방향 벽검사
    이동은 w -> B,b -> 벽검사->+(b인경우 B로 변환), w-> 벽검사->+(W) grid에 저장
    
종료검사를 언제할까? 매 경로마다?
    +의 좌표를 저장하고 매 경로마다 그 좌표가 B인지 확인

지나온 길은 어떻게 표시..?
w 는 마지막에 한번에 표시
다음 경로 그려주기, 다다음 경로 그려주기

'''
# 오답버전
from collections import deque

game = 0
while True:
    R,C = map(int,input().split())
    if R == 0 and C == 0:
        break
    game += 1
    toggle = False
    grid = [list(input()) for _ in range(R)]
    move = deque(list(input()))
    target = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'w':
                man = (i,j)
                x,y = i,j
                grid[i][j] = '.'
            elif grid[i][j] == 'W':
                man = [i,j]
                x,y = i,j
                grid[i][j] = '+'
                target.append((i,j))
            elif grid[i][j] == '+' or grid[i][j] == 'B':
                target.append((i,j))
    while move:
        current = move.popleft()
        for t in target:
            if grid[t[0]][t[1]] !='B':
                break
        else:
            toggle = True
            break

        if current == 'U':
            nx,ny = -1,0
        elif current == 'D':
            nx,ny = 1,0
        elif current == 'L':
            nx,ny = 0,-1
        elif current == 'R':
            nx,ny = 0,1

        if grid[x+(nx)*1][y+(ny)*1] == '#':
            # 벽 이동금지
            continue
        elif grid[x+(nx)*1][y+(ny)*1] == 'b':
            if grid[x+(nx)*2][y+(ny)*2] == '#' or grid[x+(nx)*2][y+(ny)*2] == 'b' or grid[x+(nx)*2][y+(ny)*2] == 'B':
                # 벽 이동금지
                continue
            elif grid[x+(nx)*2][y+(ny)*2] == '+':
                grid[x+(nx)*2][y+(ny)*2] = 'B'
                grid[x+(nx)*1][y+(ny)*1] = '.'
                x += nx
                y += ny
            else:
                grid[x+(nx)*2][y+(ny)*2]='b'
                grid[x+(nx)*1][y+(ny)*1]= '.'
                x += nx
                y += ny
        elif grid[x+(nx)*1][y+(ny)*1]=='B':
            if grid[x+(nx)*2][y+(ny)*2] == '#' or grid[x+(nx)*2][y+(ny)*2] == 'b' or grid[x+(nx)*2][y+(ny)*2] == 'B':
                #이동금지
                continue
            elif grid[x+(nx)*2][y+(ny)*2] == '+':
                grid[x+(nx)*2][y+(ny)*2] = 'B'
                grid[x+(nx)*1][y+(ny)*1] = '+'
                x += nx
                y += ny
            else:
                grid[x+(nx)*2][y+(ny)*2]='b'
                grid[x+(nx)*1][y+(ny)*1]= '+'
                x += nx
                y += ny
        else:
            x += nx
            y += ny
    for tx,ty in target:
        if x==tx and y ==ty:
            grid[x][y] = 'W'
            break
    else:
        grid[x][y] = 'w'

    if toggle:
        print(f"Game {game}: complete")
    else:
        print(f"Game {game}: incomplete")
    for r in range(R):
        print("".join(grid[r]))
    
