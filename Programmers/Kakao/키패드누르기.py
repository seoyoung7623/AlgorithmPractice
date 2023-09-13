# 키패드 누르기 Lv1
from collections import deque


# def solution(numbers, hand):
#     answer = []
#     keypad = [[1,2,3],[4,5,6],[7,8,9]['*',0,'#']]
#     move = [[1,0],[-1,0],[0,1],[0,-1]]
#     right,left = '#','*'
#     for i in numbers:
#         if i in (1,4,7):
#             answer.append('L')
#             left = i
#         elif i in (3,6,9):
#             answer.append('R')
#             right = i
#         elif i in (2,5,8,0):
#             q = deque()
#             q.append(i)
#             cnt = 0
#             L_cnt = 0
#             R_cnt = 0
#             while q:
#                 num = q.popleft()
#                 x = 1
#                 if i == 2: y = 0
#                 elif i == 5: y = 1
#                 elif i == 8: y = 2
#                 elif i == 0: y = 3
#                 for j in range(4):
#                     nx = x + move[j][0]
#                     ny = y + move[j][1]
#                     if 0<= nx < 3 and 0<= ny < 4:
#                         q.append(keypad[ny][nx])
#                         if keypad[ny][nx] == right:
#                             R_cnt = cnt
                            
#                         if keypad[ny][nx] == left:
#                             L_cnt = cnt
#                 cnt += 1
    # return answer

def solution(numbers,hand):
    answer = ''
    dic = {1:[0,0],2:[0,1],3:[0,2],
           4:[1,0],5:[1,1],6:[1,2],
           7:[2,0],8:[2,1],9:[2,2],
           '*':[3,0],0:[3,1],'#':[3,2]}

    left_s = dic['*']
    right_s = dic['#']

    for i in numbers:
        now = dic[i]
        if i in [1,4,7]:
            answer += 'L'
            left_s = now

        elif i in [3,6,9]:
            answer += 'R'
            right_s = now
        else:
            left_d = 0
            right_d = 0

            # 두 리스트 간의 거리 구하기 -> 두 점 사이의 거리 구하는 방법
            for a,b,c in zip(left_s,right_s,now): # 첫번째 : 행 두번때: 열
                left_d += abs(a-c) # 왼손과 현재 사이의 거리
                right_d += abs(b-c) # 오른손과 현재 사이의 거리

            if left_d < right_d:
                answer += 'L'
                left_s = now
            elif left_d > right_d:
                answer += 'R'
                right_s = now
            else:
                if hand == 'left':
                    answer += 'L'
                    left_s = now
                else:
                    answer += 'R'
                    right_s= now
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))