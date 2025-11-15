N,M = map(int,input().split())
items = []
dp = [0] * (M + 1)

def binary(v,c,k):
    global items
    p = 1
    while k > 0:
        cnt = min(p,k)
        items.append((v*cnt,c*cnt))
        k -= cnt
        p *= 2

for _ in range(N):
    V,C,K = map(int,input().split())
    binary(V,C,K)

for c,v in items:
    for j in range(M,c-1,-1):
        dp[j] = max(dp[j],dp[j-c] + v)
print(dp[-1])


