# 순위 Lv3
'''
아이디어 중요: 플로이드 와샬
a,b / b,c 의 경기를 알고 있을때 a,c의 경기 결과를 예측하는 문제
모든 선수에서의 경기를 알아야한다. 따라서 중간노드를 계산하는 플로이드와샬로 접근한다.
여기서 모든 경기를 알고 있는 선수를 뽑는 기준은 플로이드 와샬에서 i==j인 경우 말고 경기를 예측할수 있는 선수를 answer에 추가해준다.
그래프 저장 값: [a,b] = 1라면 [b,a] = -1
'''
def solution(n, results):
    answer = 0
    board = [[0]* (n+1) for _ in range(n+1)]
    for i,j in results:
        board[i][j] = 1
        board[j][i] = -1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = -1

    for row in board:
        if row.count(0) == 2:
            answer += 1
    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))