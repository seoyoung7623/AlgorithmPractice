from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
N = int(input())
for i in range(N):
    commend = input().split()

    if commend[0] == "push_front":
        dq.appendleft(commend[1])
    elif commend[0] == "push_back":
        dq.append(commend[1])
    elif commend[0] == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif commend[0] == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif commend[0] == "size":
        print(len(dq))
    elif commend[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif commend[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif commend[0] == "back":
        if dq:
            print(dq[len(dq)-1])
        else:
            print(-1)
    
