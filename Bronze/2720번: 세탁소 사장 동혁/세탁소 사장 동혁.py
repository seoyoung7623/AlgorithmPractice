#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2720                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2720                           #+#        #+#      #+#     #
#    Solved: 2025/04/23 09:31:41 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
T = int(input())
for test_case in range(T):
    Q,D,N,P = 0,0,0,0
    money = int(input())
    Q = money // 25
    money %= 25
    D = money // 10
    money %= 10
    N = money // 5
    money %= 5
    P = money
    print(Q,D,N,P)
    