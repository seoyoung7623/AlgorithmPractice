T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P,A,B =map(int,input().split())
    
    def binary(l,r,p):
        cnt = 0
        while l <= r:
            #print(l,r)
            cnt += 1
            mid = (l+r)//2
            if p > mid:
                l = mid
            elif p < mid:
                r = mid
            else:
                break
        return cnt
  	
    a_cnt = binary(1,P,A)
    b_cnt = binary(1,P,B)
    #print(a_cnt, b_cnt)
    
    if a_cnt < b_cnt:
        print(f"#{test_case} A")
    elif a_cnt > b_cnt:
        print(f"#{test_case} B")
    else:
        print(f"#{test_case} 0")