
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    
    def rsp(l,r):
        a,b = arr[l],arr[r]
        if (a == 1 and b == 2) or (a==2 and b ==3) or (a== 3 and b==1):
            return r
        else:
            return l
        
    def solve(l,r):
        if l == r:
            return l
        mid = (l+r)//2
        left = solve(l,mid)
        right = solve(mid+1,r)
        return rsp(left,right)
        
    print(f"#{test_case} {solve(0,N-1)+1}")
    