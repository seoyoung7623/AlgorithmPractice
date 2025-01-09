# 14891 톱니바퀴 G5
'''
구현문제
톱니가 실시간으로 회전하면 안됨!! 오류 발생가능성
회전방향을 기준으로 4개의 톱니를 탐색해 회전가능성 확인
같은지 확인하고 바로 회전하면 안됨
'''
from collections import deque

cogwheels = []
for _ in range(4):
    cogwheels.append(deque(list(map(int,input()))))
K = int(input())
arr = []
for _ in range(K):
    arr.append(list(map(int,input().split())))

def rotate(cogwheel,d):
    if d == 1:
        cogwheel.appendleft(cogwheel.pop())
    elif d == -1:
        cogwheel.append(cogwheel.popleft())

for n,d in arr:
    n = n-1
    rotate_directions = [0] * 4
    rotate_directions[n] = d

    for i in range(n,0,-1):
        if cogwheels[i][6] != cogwheels[i-1][2]:
            rotate_directions[i-1] = -rotate_directions[i]
        else:
            break

    for i in range(n,3):
        if cogwheels[i][2] != cogwheels[i+1][6]:
            rotate_directions[i+1] = -rotate_directions[i]
        else:
            break
    
    for i in range(4):
        if rotate_directions[i] != 0:
            rotate(cogwheels[i],rotate_directions[i])

answer = 0
for i in range(4):
    if cogwheels[i][0] == 1:
        answer += 2**i
print(answer)