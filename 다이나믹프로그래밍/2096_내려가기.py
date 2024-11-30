# 2096 내려가기 G5
'''
메모리 초과 주의
입력을 리스트에 저장하지 않고 바로 dp 처리를해서 메모리를 줄인다.
'''
import sys
input = sys.stdin.readline

N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for i in range(N):
    a, b, c = map(int, input().split())
    if i == 0:
        max_dp = [a, b, c]
        min_dp = [a, b, c]
    else:
        max_dp = [
            max(max_dp[0], max_dp[1]) + a,
            max(max_dp[0], max_dp[1], max_dp[2]) + b,
            max(max_dp[1], max_dp[2]) + c
        ]
        min_dp = [
            min(min_dp[0], min_dp[1]) + a,
            min(min_dp[0], min_dp[1], min_dp[2]) + b,
            min(min_dp[1], min_dp[2]) + c
        ]

print(max(max_dp), min(min_dp))
