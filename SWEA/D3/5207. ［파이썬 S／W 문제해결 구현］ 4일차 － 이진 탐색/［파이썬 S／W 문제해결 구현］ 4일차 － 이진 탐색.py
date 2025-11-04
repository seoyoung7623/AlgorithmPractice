
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    A.sort()
    
    def binary(l,r,x):
        state = ''
        while l<=r:
            mid = (l+r)//2
            if x > A[mid]:
                if state == 'r':
                    return False
                state = 'r'
                l = mid + 1
            elif x < A[mid]:
                if state == 'l':
                    return False
                state = 'l'
                r = mid - 1
            else:
                return True
       	return False
    cnt = 0
    for b in B:
        if binary(0,len(A)-1,b):
            cnt += 1
   	
    print(f"#{test_case} {cnt}")
  