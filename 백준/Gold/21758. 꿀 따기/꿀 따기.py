N = int(input())
arr = list(map(int,input().split()))

prefix_sum = [arr[0]] + ([0] * (N-1))
for i in range(1,N):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

lastfix_sum = [0] * (N)
for i in range(N-1):
    lastfix_sum[i] = prefix_sum[-1] - prefix_sum[i]

answer = 0


# 벌-벌-통
for i in range(1,N):
    total = lastfix_sum[0] + lastfix_sum[i] - arr[i]
    answer = max(total,answer)

# 통-벌-벌
for i in range(N-1):
    total = prefix_sum[-1] - arr[-1] + prefix_sum[i] - arr[i] - arr[i]
    answer = max(total,answer)

# 벌-통-벌
for i in range(1,N-1):
    total = prefix_sum[i]-arr[0]+prefix_sum[-1]-arr[-1]-prefix_sum[i-1]
    answer = max(total,answer)

print(answer)
