# 행렬 테두리 회전하기 Lv2
def solution(rows, columns, queries):
    answer = []
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = (i*columns) + j + 1

    def round(x1,y1,x2,y2):
        round_query = []
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        direct = 0
        before = 0
        x,y = x1,y1
        while True:
            nx = x + dx[direct]
            ny = y + dy[direct]
            if nx < x1 or nx > x2 or ny < y1 or ny > y2:
                direct += 1
                continue
            round_query.append(board[x][y])
            board[x][y], before = before,board[x][y]
            x = nx
            y = ny
            if x == x1 and y == y1:
                board[x][y], before = before,board[x][y] # 초기위치 이전값 설정을 안해줘서 오답이 나왔었음
                break
        return min(round_query)
    for i in queries:
        answer.append(round(i[0]-1,i[1]-1,i[2]-1,i[3]-1))
    return answer
print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))