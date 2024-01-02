# 뒤에있는 수 찾기 Lv2
'''
뒷 큰 수가 될 수를 기준으로 앞에 숫자에서 뒷 큰 수를 저장해주는 방식
pop을 통해 뒷 큰 수가 없는 인덱스를 남겨서 뒷 큰 수를 한번에 저장해준다.
'''
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    
    return answer
print(solution([9,1,5,3,6,2]))
