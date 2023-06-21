#11866 요세푸스 0 s5
# 큐

from collections import deque

N,K = map(int,input().split())

q = deque([i for i in range(1,N+1)])
list = []
n = 0
while q:
    n += 1
    if n%K == 0:
        list.append(q.popleft())
    else:
        q.append(q.popleft())
string_list = [str(e) for e in list]
print('<'+', '.join(string_list)+'>')
