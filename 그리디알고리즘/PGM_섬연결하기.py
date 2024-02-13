# 섬연결하기 Lv2
'''

1. 최단거리 구하기 이므로 우선순위큐 다익스트라로 접근했음
2. BUT 모든정점을 지나야하는 MST이므로 프림알고리즘으로 접근한다.
'''
# import heapq

# def solution(n, costs):
#     answer = 0
#     visited = [0]*(n+1)
#     graph = list([] for _ in range(n))
#     for i in costs:
#         u,v,weight = i
#         graph[u].append((weight,v))
#         graph[v].append((weight,u))

#     candidate = graph[0]
#     heapq.heapify(candidate)
#     visited[0] = 1
#     while candidate: # 힙을 모두 돌려 
#         w,v = heapq.heappop(candidate)
#         if visited[v] == 0:
#             visited[v] = 1
#             answer += w
#             for edge in graph[v]:
#                 if visited[edge[1]] == 0:
#                     heapq.heappush(candidate,edge)
#     return answer
# print(solution(4,	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

'''
3. 크루스칼 알고리즘
간선의 최소비용구하기
정렬로 인해 가중치가 작은 값부터 탐색하기 때문에 Link(가중치 시작노드가 있는 리스트) 의 값이 n-1인 경우 탐색 종료
'''
def solution(n,costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 가중치를 기준으로 정렬
    link = set([costs[0][0]]) # 가중치가 가장 작은 시작노드

    while len(link) != n: # 간선의 길이: 정점의 길이-1 띠리서 같아지먄 종료
        for v in costs:
            if v[0] in link and v[1] in link:
                # 모든 정점이 link에 있다면 사이클이 됨
                continue
            if v[0] in link or v[1] in link:
                # 하나의 정점이 연결안되어 있기때문에 연결
                # 정렬로 인해 작은 가중치부터 삽입되기때문에
                link.update([v[0],v[1]]) # update 함수 병합
                answer += v[2]
                break
    return answer