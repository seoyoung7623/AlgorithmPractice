# 2559 수열 S3
'''
포인터를 이용한 누적합

N 2이상 10^5
K 1<=K<=N
'''
N,K = map(int,input().split())
arr = list(map(int,input().split()))
max_sum = 0
for i in range(K):
    max_sum += arr[i]
next_sum = max_sum


for i in range(0,N-K):
    next_sum = next_sum - arr[i] + arr[i+K]
    max_sum = max(max_sum,next_sum)
print(max_sum)
    
