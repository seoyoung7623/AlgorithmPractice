#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1292                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1292                           #+#        #+#      #+#     #
#    Solved: 2025/04/15 09:34:07 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
A,B = map(int,input().split())

arr = []
for b in range(1,B+1):
    for _ in range(b):
        arr.append(b)
sum = 0
for i in range(A-1,B):
    sum += arr[i]
print(sum)