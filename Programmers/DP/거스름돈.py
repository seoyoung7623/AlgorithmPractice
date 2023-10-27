# 거스름돈
'''
접근방식) dp를 활용한다. dp에 저장할 값은 합의 구성의 수
2원의 경우 1+1,2의 방법이 있다.
4원의 경우 앞서 저장한 2원의 방법 모두에 2원을 붙여주면 만들수 있기때문에
2원의 방법을 저장한다. 
'''
def solution(n, money):
    dp = [1] + [0] * n
    for coin in money:
        for price in range(coin,n+1):
            if price >= coin:
                dp[price] += dp[price - coin]
    return dp[n] % 1000000007
print(solution(5,[5,1,2]))