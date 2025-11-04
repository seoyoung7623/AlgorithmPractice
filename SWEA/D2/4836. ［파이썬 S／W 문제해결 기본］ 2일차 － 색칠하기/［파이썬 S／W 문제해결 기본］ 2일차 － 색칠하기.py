T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    red = []
    blue = []
    visited = [[0] * 10 for _ in range(10)]
    cnt = 0
    
    for n in range(N):
        colors = list(map(int,input().split()))
        if colors[-1] == 1:
            red.append(colors[:-1])
        else:
            blue.append(colors[:-1])
  	
    for x1,y1,x2,y2 in red:
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                visited[i][j] = 'r'

    for x1,y1,x2,y2 in blue:
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if visited[i][j] == 'r':
                    cnt += 1
  
    print(f"#{test_case} {cnt}")
	