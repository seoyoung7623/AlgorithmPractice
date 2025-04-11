#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2693                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2693                           #+#        #+#      #+#     #
#    Solved: 2025/04/10 09:34:39 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
T = int(input())

for test_case in range(T):
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    print(A[2])

