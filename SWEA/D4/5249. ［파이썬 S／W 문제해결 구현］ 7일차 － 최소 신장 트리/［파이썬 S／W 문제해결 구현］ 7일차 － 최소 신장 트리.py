'''
크루스칼 알고리즘
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V,E = map(int,input().split())
    edge = [tuple(map(int, input().split())) for _ in range(E)]
    
    edge.sort(key = lambda x: x[2])
    print
    parent = [i for i in range(V+1)] 
    answer = 0
    picked = 0
    
    # 두 노드를 부모 노드로 변환
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if ra < rb:
            parent[rb] = ra
        else:
            parent[ra] = rb
        return True

    # 부모의 노드를 반환
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    for n1,n2,w in edge:
        if union(n1,n2):
            answer += w
            picked += 1
            if picked == V:
                break
            
    print(f"#{test_case} {answer}")
    