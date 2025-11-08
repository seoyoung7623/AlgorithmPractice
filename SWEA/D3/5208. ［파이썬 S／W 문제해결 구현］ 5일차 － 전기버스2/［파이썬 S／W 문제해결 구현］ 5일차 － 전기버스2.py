
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = list(map(int,input().split()))
    M = N[0]
    
    end = N[1]+1 # 현재 거리
    reach = N[1] # 가장 멀리갈수있는 거리
    answer = 0
    
    for i in range(2,M):
        reach = max(N[i]+i,reach)
        if end == i:
            answer += 1
            end = reach
            if end >=  M:
                break
    print(f"#{test_case} {answer}")
            
        