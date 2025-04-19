#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2581                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2581                           #+#        #+#      #+#     #
#    Solved: 2025/04/16 09:32:33 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
소수 정의: 1보다 큰 자연수 중 1과 자기자신만을 약수로 갖는 수
'''
M = int(input())
N = int(input())
total = 0
min_num = 0
toggle = False

for i in range(M,N+1):
    if i == 1:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        if not toggle:
            min_num = i
            toggle = True
        total += i

if total == 0:
    print(-1)
else:
    print(total)
    print(min_num)
