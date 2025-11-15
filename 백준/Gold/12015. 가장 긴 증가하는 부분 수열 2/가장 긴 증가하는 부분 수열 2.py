
# 위치 인덱스 리턴
def bisect_left(dp,x):
    low,high = 0,len(dp)

    while low<high:
        mid = low + (high-low) // 2
        if dp[mid] < x:
            low = mid + 1
        else:
            high = mid 
    return low

N = int(input())
arr = list(map(int,input().split()))
dp = []

for i in range(N):
    pos = bisect_left(dp,arr[i]) 
    if pos == len(dp):
        dp.append(arr[i])
    else:
        dp[pos] = arr[i]

print(len(dp))
