# x,y = [1,2]

# print(x)
# print(y)

#2023.01.04
# n = 5
# for i in (n-1,n+1,n*2):
#     print(i)

from collections import deque


q = deque([3])
q.append([5])
q.append(4)

print(q)