# 2346 풍선 터뜨리기 S3
'''
큐 rotate() 함수
'''
# from collections import deque

# N = int(input())
# balloon = list(map(int,input().split()))
# arr = []
# answer = []
# for i in range(N):
#     arr.append((balloon[i],i+1))
# balloon = deque(arr)
# num,idx = balloon.popleft()
# answer.append(idx)


# while balloon:
#     if num > 0:
#         for i in range(num):
#             balloon.append(balloon.popleft())
#         num,idx = balloon.pop()
#     else:
#         for i in range(abs(num)):
#             balloon.appendleft(balloon.pop())
#         num,idx = balloon.popleft()
#     answer.append(idx)
    
# print(*answer)

from collections import deque

N = int(input())
balloons = list(map(int,input().split()))

dq = deque(enumerate(balloons,start=1))
answer = []
while dq:
    idx,move = dq.popleft()
    answer.append(idx)

    if not dq:
        break

    if move > 0:
        dq.rotate(-(move-1)) # 현재 제거된 위치 기준 -1 보정
    else:
        dq.rotate(-move)

print(*answer)

