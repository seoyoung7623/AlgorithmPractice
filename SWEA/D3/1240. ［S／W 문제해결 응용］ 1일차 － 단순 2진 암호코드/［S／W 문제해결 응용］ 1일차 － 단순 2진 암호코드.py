T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    grid = [list(map(int,input())) for _ in range(N)]
    toggle = False
    answer = []
    
    def check(arr):
        lst = []
        cnt = 1
        for i in range(1,len(arr)):
            if arr[i] == 0:
                if arr[i-1] == 1:
                    lst.append(cnt)
                    cnt = 1
                else:
                    cnt += 1
            else:
                if arr[i-1] == 0:
                    lst.append(cnt)
                    cnt = 1
                else:
                    cnt += 1
        else:
            lst.append(cnt)
        if lst == [3,2,1,1]: return 0
        elif lst == [2,2,2,1]: return 1
        elif lst == [2,1,2,2]: return 2
        elif lst == [1,4,1,1]: return 3
        elif lst == [1,1,3,2]: return 4
        elif lst == [1,2,3,1]: return 5
        elif lst == [1,1,1,4]: return 6
        elif lst == [1,3,1,2]: return 7
        elif lst == [1,2,1,3]: return 8
        elif lst == [3,1,1,2]: return 9
                
            
    
    for i in range(N):
        for j in range(M-1,-1,-1):
            if grid[i][j] == 1 and not toggle:
                lst = [grid[i][j-55+x:j-48+x] for x in range(0, 56, 7)]
                toggle = True
                break
       	if toggle:
            break
    
    for n in lst:
        answer.append(check(n))
    odd = 0
    even = 0
    for i  in range(8):
        if i % 2 == 0:
            odd += answer[i]
        else:
            even += answer[i]
    if ((odd * 3) + even) % 10 == 0:
      	print(f"#{test_case} {sum(answer)}")
    else:
        print(f"#{test_case} 0")