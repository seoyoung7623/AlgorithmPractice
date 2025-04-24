N = int(input())
answer = []

def decimal(n):
    if n == 1 or n == 0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True

def backtracking(lst):
    # 종료 조건 (길이가 4글자인경우 종료)
    if lst:
        number = int(''.join(map(str,lst)))
        if not decimal(number):
            return
        if len(lst) == N:
            answer.append(number)
            return
    # 함수 조건
    for i in range(10):
        lst.append(i)
        backtracking(lst)
        lst.pop()


backtracking([])
for a in answer:
    print(a)