# # # 1918 후위표기식 G2
'''
스택으로 우선순위를 비교
연산자 별로 나올 가능성 판단하도록 접근
'''

calculate = input()
stack = []
res = ''
for i in calculate:
    if i.isalpha():
        res+=i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'): # 곱셈, 나눗셈의 경우 앞에 스택이 *,/ 일때만 pop()
                res += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)