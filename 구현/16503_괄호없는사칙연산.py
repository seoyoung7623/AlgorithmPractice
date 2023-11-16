# 16503 괄호없는 사칙연산
k1, o1, k2, o2, k3 = input().split()
result = []

def calculation(a,op,b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if a<0 and b>=0:
            return -(abs(a) / b)
        elif a>=0 and b<0:
            return -(a / abs(b))
        else:
            return int(a / b)


step1 = calculation(calculation(int(k1),o1,int(k2)),o2,int(k3))
step2 = calculation(int(k1),o1,calculation(int(k2),o2,int(k3)))
result.append(int(step1))
result.append(int(step2))
result.sort()
for i in result:
    print(i)