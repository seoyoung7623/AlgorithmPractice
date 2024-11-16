# 2806 N-Queen D3
'''
NxN 보드에 N개의 퀸을 안전하게 놓는 방법
'''
T=int(input())
for test_case in range(1, T+1):
    N = int(input())
    v1 = [0] * N
    v2 = [0] * 2 * N
    v3 = [0] * 2 * N
    ans = 0

    def backtracking(n):
        global ans
        if n == N:
            ans += 1
            return
        for i in range(N):
            if v1[i] == v2[n-i] == v3[n+i] == 0:
                v1[i],v2[n-i],v3[n+i] = 1,1,1
                backtracking(n+1)
                v1[i], v2[n-i], v3[n+i] = 0,0,0
    backtracking(0)
    print(f"#{test_case} {ans}")

