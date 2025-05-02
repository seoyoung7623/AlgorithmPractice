#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28279                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28279                          #+#        #+#      #+#     #
#    Solved: 2025/05/02 09:36:14 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stack = deque()

for n in range(N):
    cmd = input().rstrip().split()

    if cmd[0] == '1':
        stack.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        stack.append(int(cmd[1]))
    elif cmd[0] == '3':
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif cmd[0] == '4':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == '5':
        print(len(stack))
    elif cmd[0] == '6':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == '7':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif cmd[0] == '8':
        if stack:
            print(stack[-1])
        else:
            print(-1)