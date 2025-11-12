'''
permutation 쓰고 최소값 계산
'''
from itertools import permutations

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    
    total = int(1e5)

    for per in permutations(range(2,N+1)):
        path = [1] + list(per)+[1]
        cost = 0
        for j in range(N):
            start, end = path[j],path[j+1]
            cost += graph[start-1][end-1]
        total = min(total,cost)
            
    print(f"#{test_case} {total}")
    