# 유니온 파인드 기본 예제
n = 5  # 사람 수
parent = [i for i in range(n + 1)]  # 초기화: 각 노드가 자기 자신을 루트로 가짐

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a

# 친구 관계 추가
union(parent, 1, 2)
union(parent, 2, 3)
union(parent, 4, 5)

# 같은 그룹인지 확인
# 부모가 같은지 확인
print(find(parent, 1) == find(parent, 3))  # True
print(find(parent, 1) == find(parent, 5))  # False