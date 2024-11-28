# 두 원사이의 점수 쌍
# def solution(r1, r2):
#     answer = 0
#     for i in range(r2+1):
#         for j in range(r2+1):
#             r = (i**2+j**2)**(0.5)
#             if r1<=r<=r2:
#                 answer += 1
    
#     over=(r2-r1)+1
#     answer = answer * 4 - ((over)*4)
#     return answer
# 모든 점을 찾는 경우 시간 초과 남

import math

def solution(r1,r2):
    answer = 0
    for x in range(1,r2+1):
        y_max =  math.floor(math.sqrt(r2**2-x**2))
        y_min = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1**2-x**2)))
        answer += y_max - y_min +1
    return answer * 4

print(solution(2,3))