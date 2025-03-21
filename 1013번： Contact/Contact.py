#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1013                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1013                           #+#        #+#      #+#     #
#    Solved: 2025/03/19 20:38:21 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
정규표현식..?
패턴 100+1+ / 01
'''
import re
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    pattern = r"^(100+1+|01)+$"
    word = input().rstrip()

    if re.fullmatch(pattern, word):
        print("YES")
    else:
        print("NO")
