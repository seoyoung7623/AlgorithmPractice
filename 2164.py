#2164 카드2
from collections import deque

num = int(input())
dq = deque()
for i in range(num):
    dq.append(i+1)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
print(dq[0])

