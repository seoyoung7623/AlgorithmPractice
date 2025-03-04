# S2
'''
슬라이딩 윈도우?
누적합 아님 주의
'''
# n = int(input())
# arr = list(map(int,input().split()))
# prefix_sum = [0]*n
# prefix_sum[0] = arr[0]
# for i in range(1,n):
#     prefix_sum[i] = prefix_sum[i-1]+arr[i]


# start = 0
# end = 0
# total = arr[start]
    
'''
✅ DP
현재 상태를 이전상태의 값으로 갱신할 수 있는가
'''
n = int(input())
arr = list(map(int,input().split()))
dp = [0] * n
dp[0] = arr[0]
for i in range(1,n):
    dp[i] = max(arr[i],dp[i-1]+arr[i])
print(max(dp))