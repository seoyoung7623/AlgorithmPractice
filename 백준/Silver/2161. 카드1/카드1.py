from collections import deque

N = int(input())
q = deque([i for i in range(1,N+1)])
answer = []
while q:
    answer.append(q.popleft())
    if q:
        q.rotate(-1)
print(*answer)