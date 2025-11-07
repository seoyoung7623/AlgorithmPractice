T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    papers = list(map(int,input().split()))
    pairs = [papers[i:i+2] for i in range(0,M*2-1,2)]
    parent = [i for i in range(1+N)]    
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a,b):
        a_p = find(a)
        b_p = find(b)
        if a_p == b_p:
            return
        if a_p < b_p:
            parent[b_p] = a_p
        else:
            parent[a_p] = b_p
    
    for a,b in pairs:
        union(a,b)
    answer = set()
    for i in range(1, N+1):
        answer.add(find(i))
    print(f"#{test_case} {len(answer)}")
        
        
        