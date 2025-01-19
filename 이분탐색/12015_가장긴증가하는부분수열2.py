# 12015 가장 긴 증가하는 부분 수열 2 G2
'''
이게 왜 이분탐색?
완탐 O(N^2)
dp 가능 but O(N^2)
bisect_left 이용 : 이진탐색 알고리즘을 사용해 값이 삽입될 가장 왼쪽 위치를 찾는 기능
부분수열의 길이의 최대값을 구하기 위해 이진탐색으로 위치를 정한다.
'''

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
