T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    arr.sort(key = lambda x: (x[1],x[0]))
    cnt = 0
    end = 0
    for i in range(N):
        if arr[i][0] >= end:
            cnt += 1
            end = arr[i][1]
    print(f"#{test_case} {cnt}")
        