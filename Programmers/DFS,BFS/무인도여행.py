# 무인도 여행
'''
BFS 문제
'''
from collections import deque

def solution(maps):
    answer = []
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = deque([])
    width = len(maps[0])
    hight = len(maps)
    visited = list([0]*width for _ in range(hight))

    def BFS(i,j):
        q.append((i,j))
        visited[i][j] = 1 
        sum = int(maps[i][j])
        while q:
            x,y = q.pop()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx<0 or nx>= hight or ny<0 or ny>= width:
                    continue
                if maps[nx][ny] == 'X' or visited[nx][ny] == 1:
                    continue
                sum += int(maps[nx][ny])
                visited[nx][ny] = 1
                q.append((nx,ny))
        return sum





    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(BFS(i,j))
            else:
                visited[i][j] = 1
    if answer:
        return sorted(answer)
    else:
        return [-1]
print(solution(["XXX","XXX","XXX"]))