# 소수찾기 Lv2
# 방법1. 순열로 수를 조합후 제곱근까지 나누어떨어지지 않으면 소수판정
from itertools import permutations
global lst
lst = []

def prime_number(n):
    string = ''.join(list(n))
    num = int(string)
    if num in lst or num == 0 or num == 1:
        return False
    for i in range(2,int(num**(0.5))+1):
        if num % i == 0:
            return False
    lst.append(num)
    return True   

def solution(numbers):
    answer = 0
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            result = prime_number(j)
            if result:
                answer += 1
    return answer
print(solution("17"))

# 방법2. set의 특징을 이용한 소수구하기
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    # 에라토스테네스의 체 알고리즘 소수의 배수를 식별하고 제거
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
print(solution("41"))