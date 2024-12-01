# 9372 상근이의 비행 S4
'''
연결그래프이면서 왕복도 하나의 비행이라고 간주하기 때문에 1로 처리함.
간선의 개수를 구하면 됨!
연결그래프의 간선의 개수는 노드의 개수 -1!!
'''
T = int(input())
for test_case in range(T):
    N,M = map(int,input().split())
    for _ in range(M):
        a,b = map(int,input().split())
    print(N-1)