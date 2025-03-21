#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1769                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1769                           #+#        #+#      #+#     #
#    Solved: 2025/03/21 17:12:01 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

x = input().rstrip()
cnt = 0
answer = False
if len(x) == 1:
    if int(x)%3 == 0:
        answer = True
else:
    while 1:
        total = sum(list(map(int,x)))
        cnt += 1
        x = str(total)
        if len(x) == 1:
            if total%3 == 0:
                answer = True
            break
print(cnt)
if answer:
    print('YES')
else:
    print('NO')
    

