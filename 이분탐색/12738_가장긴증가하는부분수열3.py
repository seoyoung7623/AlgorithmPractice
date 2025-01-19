# 12738 가장 긴 증가하는 부분 수열 3
'''
이번에는 수열에 음수가 포함
그럼 새로 들어오는 수는 작은수로 갱신해야 다음수가 더 작은수로 갱신할 수 있음
ex) -20 의 다음수는 -10 or 10 가능성이 있다.
'''
N = int(input())
arr = list(map(int,input().split()))
dp = []

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

for i in range(N):

    pos = bisect_left(dp,arr[i]) 
    if pos == len(dp):
        dp.append(arr[i])
    else:
        if dp[pos] > arr[i]:
            dp[pos] = arr[i]
    
print(len(dp))