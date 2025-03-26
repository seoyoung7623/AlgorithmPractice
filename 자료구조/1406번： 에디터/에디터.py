#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1406                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1406                           #+#        #+#      #+#     #
#    Solved: 2025/03/25 09:11:54 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
리스트로 시간초과가 날까?
커서의 위치 배열에서 삽입, 삭제, 이동
리스트에서 insert하면 시간초과 나지 않나?
insert del O(N)

2개의 dequeue 이용
'''

from collections import deque
import sys
input = sys.stdin.readline

word = input().rstrip()
leftq = deque(list(word))
rightq = deque([])
M = int(input())
for test_case in range(M):
    order = input().rstrip()
    if order[0] == 'L':
        if leftq:
            rightq.appendleft(leftq.pop())
    elif order[0] == 'D':
        if rightq:
            leftq.append(rightq.popleft())
    elif order[0] == 'B':
        if leftq:
            leftq.pop()
    elif order[0] =='P':
        leftq.append(order[-1])
print(''.join(leftq+rightq))
