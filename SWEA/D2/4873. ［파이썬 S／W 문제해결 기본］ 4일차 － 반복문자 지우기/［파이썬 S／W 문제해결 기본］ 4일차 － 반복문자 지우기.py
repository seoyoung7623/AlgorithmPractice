T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = list(input())
    toggle = True
    
    while toggle:
        for i in range(len(N)-1):
            if N[i] == N[i+1]:
                del N[i:i+2]
                break
        else:
            toggle = False
    
    print(f"#{test_case} {len(N)}")
        
        