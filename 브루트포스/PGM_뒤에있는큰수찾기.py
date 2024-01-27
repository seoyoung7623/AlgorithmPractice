# 프로그래머스) 뒤에 있는 큰수 찾기
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i) 
    return answer