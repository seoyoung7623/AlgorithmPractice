'''
그리디 요격시스템
요격의 길이 측정 방법
BFS로 요격의 길이 측정
끝나는 점을 기준으로 정렬
'''
from collections import deque

def solution(land):
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    hight = len(land)
    width = len(land[0])
    visited = [[0]*width for _ in range(hight)]
    
    # print(width, hight)
    def bfs(start_x,start_y,visited):
        q = deque([])
        q.append((start_x,start_y))
        visited[start_x][start_y] = 1
        cnt = 1
        min_w = start_y
        max_w = start_y
        while q:
            x,y = q.pop()
            for k in range(4):
                nx = x + directions[k][0]
                ny = y + directions[k][1]
                
                if 0 <= nx < hight and 0 <= ny < width and visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    min_w = min(min_w,ny)
                    max_w = max(max_w,ny)
                    cnt += 1
        return (cnt,min_w,max_w)
    lst = []
    for i in range(hight):
        for j in range(width):
            if land[i][j] == 1 and visited[i][j] == 0:
                lst.append(bfs(i,j,visited))
                
    answer = [0] * width
    for cnt,start,end in lst:
        for i in range(start,end+1):
            answer[i] += cnt
    # print(lst)
    return max(answer)
