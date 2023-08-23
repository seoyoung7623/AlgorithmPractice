# 5430 AC G1
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

# 접근 방식 reverse를 계속해주지 않고, 마지막에 한번만 해주면 된다!
for t in range(T):
    read = input().strip()
    num = int(input())
    lst = deque(input().rstrip()[1:-1].split(','))
    rev = 0
    flag = True

    if num == 0:
        lst = deque()

    for i in read:
        if i == "R":
            rev += 1
        if i =="D":
            if len(lst)<1:
                print("error")
                flag = False
                break
            else:
                if rev%2 == 0: # 짝수인 경우
                    lst.popleft()
                else:
                    lst.pop()
    
    if flag:
        if rev %2 != 0: #짝수가 아닌 경우
            lst.reverse()
        print('['+','.join(lst)+']')



    

# for i in range(T):
#     read = input().strip()
#     num = int(input())
#     lst = deque(input().rstrip()[1:-1].split(','))
#     for j in range(len(read)):
#         if read[j] == 'R':
#             lst.reverse()
#         if read[j] == 'D':
#             if lst:
#                 lst.popleft()
#             else:
#                 print("error")
#                 break
#     else:
#         print("["+",".join(lst)+']')