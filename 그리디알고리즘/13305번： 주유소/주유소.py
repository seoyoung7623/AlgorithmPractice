#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13305                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13305                          #+#        #+#      #+#     #
#    Solved: 2025/03/28 15:14:31 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
이게 그리디?
5 2 4 1
'''
import sys
input = sys.stdin.readline
N = int(input())
roads = list(map(int,input().split()))
prices = list(map(int,input().split()))
total = 0
min_price = 1e10
for i in range(N-1):
    min_price = min(min_price,prices[i])
    total += min_price * roads[i]
print(total)
