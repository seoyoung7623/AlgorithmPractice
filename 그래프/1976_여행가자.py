# 1976 여행가자 G4
'''
Union-Find 문제
출력이 단순히 가능 or 불가능 문제이기 때문이다.
'''
N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a


for n in range(N):
    road = list(map(int,input().split()))
    road.insert(0,0)
    for i in range(1,N+1):
        if road[i] == 1:
            union(n+1,i)

plan = list(map(int,input().split()))
root = find(plan[0])
for p in plan:
    if find(p) != root:
        print('NO')
        break
else:
    print('YES')