#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18258                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18258                          #+#        #+#      #+#     #
#    Solved: 2025/03/26 16:12:56 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stack = deque([])

for i in range(N):
    word = input().rstrip().split()
    if word[0] == 'push':
        stack.append(word[-1])
    elif word[0] == 'pop':
        if stack:
            print(stack.popleft())
        else:   
            print(-1)
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif word[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif word[0] == 'back':    
        if stack:
            print(stack[-1])
        else:
            print(-1)
    