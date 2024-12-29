# PGM 카카오 등산코드 정하기 Lv3
''' 나의 접근 방법
가장 긴 거리가 가장 짧은 루트
최단거리
그 코스 그대로 돌아오기
DFS로 해보자
'''
# def solution(n, paths, gates, summits):
#     answer = []
#     table = [[] for _ in range(n+1)]
#     for i,j,w in paths:
#         table[i].append((j,w))
#         table[j].append((i,w))
    
#     def DFS(x,cost,visited):
#         if cost!=0 and x in gates:
#             return
#         if x in summits:
#             answer.append((x,cost))
#             answer.sort(key=lambda x:(x[1],x[0]))
#             return
#         for y,w in table[x]:
#             if visited[y] == 0:
#                 if answer and w>answer[0][1]:
#                     continue
#                 next_cost = max(cost,w)
#                 visited[y] = 1
#                 DFS(y,next_cost,visited)
#                 visited[y] = 0

            
#     for gate in gates:
#         visited = [0]*(n+1)
#         visited[gate] = 1
#         DFS(gate,0,visited)
#     answer.sort(key=lambda x:(x[1],x[0]))
#     return list(answer[0])

# print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))

''' 참고풀이
다익스트라로 접근 최단경로를 저장하는것이아닌 intensity를 저장한다.
+ set으로 변경해 시간을 줄여야함, 테스트 25번에서 시간초과가 발생했다.
탐색을 위해서는 list 보다 set이 빠르다.
ex) if x in summits_set 조건문 if in을 이용할때는 set을 사용하자.
'''
from collections import deque
import heapq

def solution(n, paths, gates, summits):
    INF = 1e8
    def get_min_intensity():
        pq = []
        visited = [INF]*(n+1)

        # 초기시작: 입구 gate 넣기
        for gate in gates:
            heapq.heappush(pq,(0,gate))
            visited[gate] = 0
        
        while pq:
            intensity,x = heapq.heappop(pq) #여기서 pop되는게 intensity!!
            # 봉우리에 도착하면 멈춤
            if x in summits_set or intensity>visited[x]:
                continue

            for w,next in graph[x]:
                new_intensity = max(w,intensity)
                if new_intensity < visited[next]:
                    visited[next] = new_intensity
                    heapq.heappush(pq,(new_intensity,next))
        
        min_intensity = [0,INF]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]
        return min_intensity
            

    summits.sort()
    summits_set = set(summits)
    graph = [[] for _ in range(n+1)]
    for i,j,w in paths:
        graph[i].append((w,j))
        graph[j].append((w,i))
    
    return get_min_intensity()
print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))