#다리 건너기 '조합'이용

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

num = int(input())

for _ in range(num):
    n1,n2 = map(int, input().split())
    b = factorial(n2) // (factorial(n1)*factorial(n2-n1))
    print(b)

