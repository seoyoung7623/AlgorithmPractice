# 플로이드 워셜 알고리즘
INF = int(1e9)
n,m = map(int,input().split()) # 노드 수, 간선의 수
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트를 만들고, 무한으로 초기화
for a in range(1,n+1): # 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b,c = map(int,input().split()) # a에서 b로 가는 비용은 c
    graph[a][b] = c

for k in range(1,n+1): # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] ==min(graph[a][b],graph[a][k]+graph[k][b])

# 결과 출력
for a in range(1,n+1):
    for b in range(1+n+1):
        if graph[a][b] == INF:
            print("도달할 수 없습니다.",end=" ")
        else:
            print(graph[a][b],end=" ")
    print()

