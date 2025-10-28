
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    T = int(input())
    answer = 0
    grid = [list(map(int,input().split())) for _ in range(100)]
    
    for i in range(100):
        answer = max(sum(grid[i]), answer)
    
    for i in range(100):
        answer = max(sum(grid[j][i] for j in range(100)), answer)

    answer = max(sum(grid[i][i] for i in range(100)), answer)
    answer = max(sum(grid[i][99 - i] for i in range(100)), answer)
    print(f"#{test_case} {answer}")