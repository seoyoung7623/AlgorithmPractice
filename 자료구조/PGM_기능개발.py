# 기능개발 Lv2 스택/큐
import math

def solution(progresses, speeds):
    stack = []
    answer = []
    for i,j in zip(progresses,speeds):
        num = math.ceil((100-i)/j)
        stack.append(num)
    cnt = 0
    while stack:
        if stack[-1] == max(stack):
            stack.pop()
            answer.append(cnt+1)
            cnt = 0
        else:
            stack.pop()
            cnt += 1 
    return answer[::-1]
print(solution([95, 90, 99, 99, 80, 99],[1,1,1,1,1,1]))