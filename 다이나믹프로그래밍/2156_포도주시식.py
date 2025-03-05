# S1
'''
https://www.acmicpc.net/problem/2156
연속 1,2 잔의 포도주를 마신다. 연속 3잔은 불가능
DP문제
현재의 선택에 따라 다음 상태가 달라진다.
1. 현재잔을 마시는 경우
    a. 1번째 잔인 경우
    b. 2번째 잔인 경우
2. 현재잔을 마시지 않는 경우

3가지 경우의 최대값으로 갱신한다.
'''
n = int(input())
arr = [int(input()) for _ in range(n)]
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
else:
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(dp[0]+arr[2],dp[1],arr[1]+arr[2])

    for i in range(3,n):
        # 2번째 잔인 경우, 1번째 잔인 경우, 현재 잔을 마시지 않는 경우
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i],dp[i-1])
    print(dp[-1])