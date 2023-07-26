# 9663 N-Queen G4
# 백트래킹

N = int(input())
ans = 0
v1 = [0] *N
v2 = [0] * (N*2)
v3 = [0] * (N*2)

def dfs(n): #여기서 n은 현재 탐색하고 있는 열
    global ans
    if n==N: #종료조건
        ans +=1
        return
    for i in range(N): # 함수호출 조건
        if v1[i] == v2[n+i] == v3[n-i] == 0:
            v1[i] = v2[n+i] = v3[n-i] = 1
            dfs(n+1)
            v1[i] = v2[n+i] = v3[n-i] = 0

dfs(0)
print(ans)