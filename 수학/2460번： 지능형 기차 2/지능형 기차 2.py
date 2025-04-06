#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2460                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2460                           #+#        #+#      #+#     #
#    Solved: 2025/04/04 09:30:55 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
total = 0
answer = 0
for i in range(10):
    _out,_in = map(int,input().split())
    total += _in
    total -= _out
    answer = max(answer,total)
print(answer)
    