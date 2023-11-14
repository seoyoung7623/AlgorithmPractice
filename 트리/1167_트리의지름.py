# 1167 트리의 지름 G2
v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    pairs = list(map(int,input().split()[:-1])) # 맨마지막 -1를 제외한 숫자들을 리스트로 가져옴
    for i in range(1,len(pairs),2):
        graph[pairs[0]].append((pairs[i],pairs[i+1]))

def DFS(x,wei): # 다음 트리, 경로값
    for i in graph[x]:
        a,b = i
        if distance[a] == -1:
            distance[a] = wei + b
            DFS(a,wei+b)


    
distance = [-1] * (v+1)
distance[1] = 0
DFS(1,0)

idx = distance.index(max(distance))
distance = [-1] * (v+1)
distance[idx] = 0
DFS(idx,0)

print(max(distance))

