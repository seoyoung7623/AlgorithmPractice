# 전력망을 둘로 나누기 Lv2 
'''
1. 내 접근 방법: 전력망 완전탐색, BFS 접근
'''
# from collections import deque    
    
# def solution(n, wires):
#     def bfs(start,a,b,visited):
#         q = deque()
#         q.append(start)
#         visited[start] = 1
#         while q:
#             n = q.popleft()
#             for i in graph[n]:
#                 if (n == a and i == b) or (n== b and i == a) or visited[i] == 1:
#                     continue
#                 visited[i] = 1
#                 q.append(i)
#     answer = []
#     graph = list([] for _ in range(n+1))
#     for i in wires:
#         a,b = i
#         graph[a].append(b)
#         graph[b].append(a)
#     for i in range(1,n+1):
#         for j in graph[i]:
#             visited = [0]*(n+1)
#             bfs(1,i,j,visited)
#             if visited[1:] == 1:
#                 continue
#             else:
#                 num1 = visited.count(1)
#                 answer.append(abs(num1-(n-num1)))
            
#     return min(answer)
# print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))

'''
트리구조를 이용한 union-find 방법: 같은 영역 트리의 세트를 기준으로 트리의 길이와 상위 노드를 알수있다.
'''
uf = []

def find(a): # 상위요소 추척
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb] #음수일수록 상위로드
    uf[pb] = pa # 상위노드를 지정해줌

def solution(n, wires):
    global uf
    answer = int(1e9) # 초기 무한대로 설정
    k = len(wires) # 전력망의 개수
    for i in range(k):
        uf = [-1 for _ in range(n+1)] # 전력망 만큼 -1
        tmp = [wires[x] for x in range(k) if x != i] # 연결 선 2차원 배열 생성 i번째씩 제거후 탐색
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0] # 음수인값 2개
        answer = min(answer, abs(v[0]-v[1]))

    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))