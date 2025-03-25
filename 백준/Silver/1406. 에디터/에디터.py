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
