# G4 https://www.acmicpc.net/problem/2293
'''
동전을 사용하해서 만들수있는 값의 경우의 수를 출력해라
✅ DP
매 금액마다 동전을 추가하는게 아니라 동전을 기준으로 금액을 만듦
1,2원이 있고 4원을 만들어라
1원을 기준으로 4원까지 1, 1+1, 1+1+1, 1+1+1+1
2원을 기준으로 4원까지 1, 1+1/2, 1+1+1/1+2, 1+1+1+1/1+1+2/2+2
'''
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
money = list(int(input()) for _ in range(n))
dp = [1]+[0]*k
for coin in money:
    for c in range(coin,k+1):
        dp[c] += dp[c-coin]
print(dp[k])
