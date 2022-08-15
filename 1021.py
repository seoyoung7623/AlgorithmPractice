#1021 회전하는 큐 다시

# n, c = map(int,input().split())
# q = [i+1 for i in range(n)]
# q1 = q.copy()
# num = list(map(int,input().split()))
# cnt = 0

# for j in range(len(num)):
#     if q[0] == num[j]:
#             q.remove(num[j])
#             continue
#     for i in range(len(q)):
#         if q[(n-1)//2] >= num[j]:
#             #왼쪽이동
#             if i == len(q)-1:
#                 q[i] = q1[0]
#             else:
#                 q[i] = q1[i+1]
#         else:
#             #오른쪽이동
#             if i == len(q)-1:
#                 q[0] = q1[i]
#             else:
#                 q[i+1] = q1[i]
#     cnt += 1
#     if q[0] == num[j]:
#             q.remove(num[j])
#             continue
# print(cnt)

from collections import deque

n, c = map(int,input().split())
num = list(map(int,input().split()))
dq = deque([i+1 for i in range(n)])

cnt = 0
for i in num:
    while 1:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) <len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt +=1
            else:
                while dq[0] !=i:
                    dq.appendleft(dq.pop())
                    cnt +=1
print(cnt)
