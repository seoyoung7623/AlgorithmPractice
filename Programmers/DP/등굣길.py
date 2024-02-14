# 등굣길 Lv3 
# def solution(m, n, puddles):
#     answer = 0
#     graph = list([0]*(m+1) for _ in range(n+1))
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if i == 1 or j == 1:
#                 graph[i][j] = 1
#                 continue
#             if [i,j] in puddles:
#                 graph[i][j] = 0
#                 continue
#             if i-1 <= 0 or j-1 <= 0:
#                 continue
#             graph[i][j] = max(graph[i][j],graph[i-1][j] + graph[i][j-1])         
#     answer = (graph[-1][-1])%1000000007
#     return answer
# print(solution(5,3,[[2, 2],[2,3],[2,4],[3,3]]))

def solution(m, n, puddles):
    answer = 0
    graph = list([0]*(m+1) for _ in range(n+1))
    graph[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                continue
            if [j,i] in puddles:
                graph[i][j] = 0
            else:
                graph[i][j] = (graph[i-1][j] + graph[i][j-1])&1000000007
    return graph[n][m]

print(solution(5,3,[[2, 2],[2,3],[2,4],[3,3]]))