# 아이템 줍기 Lv3
'''
테두리의 겹치지 않는 부분을 구하기 위해 좌표를 *2배류 초기 설정
이후 테두리를 따라 BFS 진행 후 결과값에 //2를 해주는것이 답이 된다
'''
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = list([-1]*102 for _ in range(102))
    for box in rectangle:
        x1,y1,x2,y2 = map(lambda x:x*2,box)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    graph[i][j] = 0
                # 테두리 설정
                elif graph[i][j] != 0:
                    graph[i][j] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque([[characterX*2,characterY*2]])
    visited = [[1]*102 for i in range(102)]
    visited[characterX*2][characterY*2] = 0

    while q:
        x,y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if graph[nx][ny] == 1 and visited[nx][ny] == 1: # 테두리, 방문하지 않은 경우
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1
    return answer
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))