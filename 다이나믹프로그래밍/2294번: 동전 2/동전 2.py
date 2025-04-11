#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2294                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2294                           #+#        #+#      #+#     #
#    Solved: 2025/04/09 09:32:06 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
최소개 동전으로 합만들기
DP다
'''
n,k = map(int,input().split())
INF = int(1e6)
dp = [INF]*(k+1)
dp[0] = 0 # 0원은 0개!
coins = [int(input()) for _ in range(n)]

for coin in coins:
    for i in range(coin,k+1):
        dp[i] = min(dp[i],dp[i-coin]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])