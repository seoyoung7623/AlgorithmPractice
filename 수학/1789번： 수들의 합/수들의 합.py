#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1789                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1789                           #+#        #+#      #+#     #
#    Solved: 2025/04/04 09:39:10 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
서로 다른 N개의 자연수의 합
'''
N = int(input())
total = 0
i = 0
while 1:
    if total > N:
        print(i-1)
        break
    elif total == N:
        print(i)
        break
    i += 1
    total += i

# 등차수열의 합
s = int(input())
n= 1
while n *(n+1) / 2 <= s:
    n += 1
print(n-1)
       