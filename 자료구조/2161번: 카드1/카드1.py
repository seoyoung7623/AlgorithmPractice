#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2161                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2161                           #+#        #+#      #+#     #
#    Solved: 2025/04/06 21:43:23 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
1234567
1 345672
3 56724
5 7246
7 462
4 26
2 6
'''
from collections import deque

N = int(input())
q = deque([i for i in range(1,N+1)])
answer = []
while q:
    answer.append(q.popleft())
    if q:
        q.rotate(-1)
print(*answer)


