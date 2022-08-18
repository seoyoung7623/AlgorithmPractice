# 10845큐
# str = sys.stdin.readline().split() 입력받을때 이거써야 시간 초과가 안됨
import sys

num = int(input())
q = []

for _ in range(num):
    str = sys.stdin.readline().split()
    if str[0] == 'push':
        q.append(str[1])
    elif str[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.remove(q[0])
    elif str[0] == "size":
        print(len(q))
    elif str[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif str[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif str[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q)-1])


