# 자릿수더하기 
def solution(n):
    n = str(n)
    answer = 0
    for i in n:
        answer += int(i)
    return answer
print(solution(1234))