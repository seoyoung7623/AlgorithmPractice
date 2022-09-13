from collections import deque
from operator import ne


graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# 큐,스택을 활용한 DFS구현
# 리스트 활용
# def dfs(graph, start_node):
#     need_visited,visited = list(),list()
#     need_visited.append(start_node) #시작노드 지정

#     #아직 방문이 필요한 노드가 있으면,
#     while need_visited:
#         node = need_visited.pop()

#         if node not in visited:
#             visited.append(node)
#             need_visited.extend(graph[node])
#     return visited
# print(dfs(graph, 'A'))

#deque를 활용한 구현
def dfs2(graph,start_node):
    visited = []
    need_visited = deque()

    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited
print(graph,'A')


#재귀함수를 이용
def dfs_recursive(graph,start,visited =[]):
    visited.append(start) #append왜 안됨? 리스트 인식이 안되는 것 같은데

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph,node,visited)
    return visited