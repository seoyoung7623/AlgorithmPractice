'''
포인터
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    c = list(map(int,input().split()))
    w = list(map(int,input().split()))
    
    c.sort(reverse = True)
    w.sort(reverse = True)
    
    a,b = 0,0
    total = 0
    
    while a< N and b<M:
        if c[a] <= w[b]:
            total += c[a]
            a += 1
            b += 1
        else:
            a += 1
            
    print(f"#{test_case} {total}")
            
            