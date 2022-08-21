#1966 프린터 큐
# from collections import deque

# testcase = int(input())

# for i in range(testcase):
#     cnt = 0
#     n, m = map(int,input().split())
#     dq = deque(map(int,input().split()))
#     dq[m] = -1
#     for j in range(len(dq)):
#         if dq[0] == -1:
#             dq.popleft()
#             cnt += 1
#             break
#         if dq[0] < max(dq):
#             dq.append(dq.popleft)
#         else:
#             dq.popleft()
#             cnt += 1
#     print(cnt)

#중요로 리스트를 만들고 찾으려는 값의 위치를 나타내는 리스트도 만들어준다.
testcase = int(input())

for i in range(testcase):
    cnt = 0
    n, m = map(int,input().split())
    myq = list(map(int,input().split()))
    qIdx = [0 for i in range(n)]
    qIdx[m] = -1
    while 1:
        if myq[0] == max(myq):
            cnt +=1
            if qIdx[0] == -1:
                print(cnt)
                break
            myq.pop(0)
            qIdx.pop(0)
        else:
            myq.append(myq.pop(0))
            qIdx.append(qIdx.pop(0))


