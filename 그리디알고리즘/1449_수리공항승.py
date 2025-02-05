# 1449 수리공항승 S3
N,L = map(int,input().split())
pipe = list(map(int,input().split()))
pipe.sort()

stand,cnt = 0,0
for i in range(N):
    if stand <= pipe[i]:
        cnt += 1
        stand = pipe[i] + L
print(cnt)