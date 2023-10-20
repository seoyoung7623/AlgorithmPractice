# 16954 A->B S2
from collections import deque

A,B = map(int,input().split())
q = deque()
q.append([A,1])

while q:
    x,cnt = q.popleft()
    if x==B:
        print(cnt)
        break
    if x>B:
        continue
    # elif x%2==0 and x>B:
    #     print(-1)
    #     break #이건 왜 안됨..
    q.append([x*2,cnt+1])
    q.append([x*10+1,cnt+1])
else:
    print(-1)

