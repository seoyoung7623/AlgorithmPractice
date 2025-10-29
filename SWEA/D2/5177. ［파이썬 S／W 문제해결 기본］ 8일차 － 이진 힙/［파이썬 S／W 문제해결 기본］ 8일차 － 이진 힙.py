import heapq

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    N = int(input())
    numbers = list(map(int,input().strip().split()))
    
    hq = []
    for num in numbers:
        heapq.heappush(hq,num)
    last = N-1
    while last > 0:
        last = (last-1)//2
        answer += hq[last]
    print(f"#{test_case} {answer}")
    
    