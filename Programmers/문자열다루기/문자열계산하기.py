# 문자열 계산하기
def solution(my_string):
    answer = 0
    my_string = my_string.split()
    for i in range(len(my_string)):
        if i == 0:
            answer = int(my_string[0])
        if my_string[i] == '+':
            answer += int(my_string[i+1])
        elif my_string[i] == '-':
            answer -= int(my_string[i+1])
    return answer
print(solution("3 - 4"))