# 11053 가장 긴 증가하는 부분 수열 S2
'''
dp r값을 모두 1로 초기화하고 lst에 값을 비교했을때 i가 더 크면 dp + 1을 해준다
'''
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
dp = [1]* N
for i in range(1,N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))