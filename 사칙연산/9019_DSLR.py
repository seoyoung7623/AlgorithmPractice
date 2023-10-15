# 9019 DSLR G4
# BFS
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())   
for _  in range(T):
    A,B = map(int,input().split())

    visited = [False for _ in range(10001)] #모든 수 체크
    q = deque()
    q.append([A,''])
    visited[A] = True
    while q:
        num, command = q.popleft()

        if num == B: # 종료조건
            print(command)
            break
        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append([d,command+'D']) #command+D!
        s = (num-1)%10000
        if not visited[s]:
            visited[s] = True
            q.append([s,command+'S'])
        l = num // 1000 + (num%1000) * 10 # l 수식으로 접근 생각!
        if not visited[l]:
            visited[l] = True
            q.append([l,command+'L'])
        r = num //10 + (num %10)*1000
        if not visited[r]:
            visited[r] = True
            q.append([r,command+'R'])


    

