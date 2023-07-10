# 프렌즈4블록

# def solution(m, n, board):
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#     answer = 0

#     visited = [False*n for i in range(m)]
#     test = False

#     # 정사각형으로 같은 캐릭터가 있는지 체크
#     for i in range(m):
#         for j in range(n):
#             board[i][j]
#             visited[i][j] = True

#             for k in range(4):
#                 nx = j+dx[k]
#                 ny = i+dy[k]
#                 if board[ny][nx] == board[i][j]:
#                     i = ny
#                     j = nx
#                 else:
#                     continue
#                 test = True

#             if test:
#                 for k in range(4):
#                     nx = j+dx[k]
#                     ny = i+dy[k]
#                     visited[ny][nx] = True

#     # 중복허용하여 정사각형의 캐릭터들을 삭제하고 수를 셈
#     for i in range(m):
#         for j in range(n):
#             if visited[i][j] == True:
#                 board[i][j] = 0
#                 answer += 1

#     # 블록을 위에서 아래로 당김 (구현 못함)
#     for i in range(n):
#         for j in range(m,0,-1):
#             if board[j][i] == 0:
      

#     return answer


def solution(m, n, board):
    answer = 0
    rm = set() # 블록은 중복을 허용해도 되기때문에 집합으로 저장

    # 문자열을 리스트로 바꿔준다!!
    for i in range(m):
        board[i] = list(board[i])
    
    # 4블록 체크
    while True:
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                if t == []:
                    continue
                if board[i][j+1] == t and board[i+1][j] == t and board[i+1][j+1] == t:
                    rm.add((i,j))
                    rm.add((i+1,j))
                    rm.add((i,j+1))
                    rm.add((i+1,j+1))
                    # 하나의 격자마다 주변격자를 탐색해서 정사각형 블록인 경우 기억장치에 저장
                    # 블록을 이동해서 탐색할 필요없음! ex) dx,dy[0,1,0,-1]

        # 정사각형 블록의 개수를 찾은 후 블록 제거
        if rm:
            answer += len(rm)
            for i,j in rm:
                board[i][j] = []
            rm = set()
        else:
            return answer
        
        # 블록을 아래의 빈 칸에 내리는 작업
        while True:
            moved = 0
            for i in range(m-1): #가장 위애서 부터 탐색(나는 아래부터 생각했음)
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        # 블록을 내리는 방법:
                        # 현재 블록이 있고 아래 칸에 블록이 없는경우 블록을 내림
                        # 이 작업을 모든 칸에서 반복하면 모든 블록을 아래로 내릴 수 있음!! -> 이 방법을 생각 못함
                        moved = 1
            if moved == 0:
                break

