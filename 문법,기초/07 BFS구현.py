# BFS구현
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

def bfs(graph,start_node):
    need_visited , visited = [],[]
    need_visited.append(start_node)

    while need_visited:
        node = need_visited[0]
        del need_visited[0] #받고 삭제

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

print(bfs(graph, 'A'))

#BFS와 DFS의 큰 파이점은 while 다음에 어떤 자료를 우선적으로 추출하느냐이다.
# DFS는 가장끝에 있는 데이터를 기준으로 추출
# BFS는 가장 처음에 있는 인자를 받는다.