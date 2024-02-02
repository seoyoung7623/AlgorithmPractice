# 카펫 Lv2
def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for a in range(1,total+1):
        b = total//a
        if brown == 2 * (a+b)-4 and a>=b and a*b == total:
            answer = [a,b]
            break
    return answer
print(solution(8,1))