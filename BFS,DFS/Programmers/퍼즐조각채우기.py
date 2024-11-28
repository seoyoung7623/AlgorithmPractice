# 퍼즐조각채우기 Lv3
'''
BFS를 쓰긴하지만 빡구현문제에 가까움
'''
from collections import deque

def solution(game_board, table):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    # 1. 보드를 돌면서 비어있는 곳을 만나면 BFS를 시작해 엠티보드에 넣어준다.
    def find_block(board,f):
        empty_list = []
        start = [0,0]
        visited = list([0]*len(board[0]) for _ in range(len(board)))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == f and not visited[i][j]:
                    q = deque([[i,j]])
                    lst = [[i,j]]
                    visited[i][j] = 1

                    while q:
                        x,y = q.popleft()

                        for k in range(4):
                            nx = dx[k] + x
                            ny = dy[k] + y

                            if (nx<0 or nx>=len(board) or ny<0 or ny>=len(board[0])) or board[nx][ny] == f^1 or visited[nx][ny] == 1:
                                continue
                            q.append([nx,ny])
                            visited[nx][ny] = 1
                            lst.append([nx,ny])
                    empty_list.append(lst)
        
        return empty_list
    
    # 2. 2차원 리스트로 블록을 묶음 
    '''
    묶음들의 x갑과 y값 각각의 최대 - 최소 + 1을 하면 2차원리스트의 길이를 구할 수 있음
    기본 블록의 좌표는 길이의 최소를 빼주면 테이블에서의 좌표를 구할 수 있다.
    (2차원 리스트로 새로 묶기 -> 방법생각하기 어려움)
    '''
    def make_table(block):
        x,y = zip(*block)
        hight = max(x) - min(x) + 1
        width = max(y) - min(y) + 1
        table = [[0]*width for _ in range(hight)]

        for i,j in block:
            i,j = i-min(x),j-min(y)
            table[i][j] = 1  
        return table
    
    # 3. 블록을 회전
    '''
    90도 회전 방법 : (i,j) -> (j,len(가로길이)-1-i) # 행렬의 성질 이용
    '''
    def rotate(table):
        rotate = list([0]*len(table) for _ in range(len(table[0]))) # 회전 시 테이블의 가로,세로 반대 주의!
        count = 0

        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == 1:
                    count += 1
                rotate[j][len(table)-1-i] = table[i][j]
        return rotate,count

    answer = 0
    empty_blocks = find_block(game_board,0) #테이블
    puzzles = find_block(table,1) # 블록

    for empty in empty_blocks:
        filled = False
        table = make_table(empty)

        for puzzle_origin in puzzles:
            if filled == True:
                break
            puzzle = make_table(puzzle_origin)
            for i in range(4): # 블록 회전
                puzzle,count = rotate(puzzle)

                if table == puzzle:
                    answer += count
                    puzzles.remove(puzzle_origin)
                    filled = True
                    break
    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
