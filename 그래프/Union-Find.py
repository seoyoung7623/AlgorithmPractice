# Union-Find 연습예제
n = 5
parent = [i for i in range(n+1)] # 초기화: 각 노드가 자기 자신을 루트로 가짐

def find(parent, x):
    if parent[x] != x: # 다른 루트가 존재하는것
        parent[x] = find(parent,parent[x]) 
    return parent[x]

def union(parent, a, b):
    root_a = find(parent,a)
    root_b = find(parent,b)
    if root_a != root_b: # 합치기로했는데 루트가 다르면 갱신해준다.
        parent[root_b] = root_a

union(parent,1,2)
union(parent,2,3)
union(parent,4,5)


print(f'1,3 은 같은 그룹인가요?: {find(parent,1) == find(parent,3)}')
print(f'1,5 는 같은 그룹인가요?: {find(parent,1) == find(parent,5)}')