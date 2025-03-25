import sys
input = sys.stdin.readline

N,M = map(int,input().split())
parent = [i for i in range(N+1)]

def union(a,b):
    a = find(a) # 부모값
    b = find(b) # 부모값
    if a != b:
        parent[b] = a # 부모값으로 갱신

# 주의!
def find(x):
    if parent[x] != x: 
        parent[x] = find(parent[x])
    return parent[x] # 부모 루트값

for test_case in range(M):
    op,a,b = map(int,input().split())
    if op == 0:
        union(a,b)
    elif op == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')