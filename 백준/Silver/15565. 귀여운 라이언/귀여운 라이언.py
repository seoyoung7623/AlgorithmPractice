import sys
input = sys.stdin.readline

N,K = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = 0
diff = []

for i in range(N):
    if arr[i] == 1:
        diff.append(i)

if len(diff) < K:
    print(-1)
    exit()

answer = float('inf')
l = len(diff)

for i in range(l-K+1):
    answer = min(diff[i+K-1] - diff[i] + 1,answer)
    
print(answer)

    
