N = int(input())
line = input()
dic = {}
for i in range(N):
    dic[chr(i+65)] = int(input())
stack = []

for i in line:
    if i =='+':
        a,b = stack.pop(),stack.pop()
        stack.append(a+b)
    elif i =='*':
        a,b = stack.pop(),stack.pop()
        stack.append(a*b)
    elif i =='-':
        a,b = stack.pop(),stack.pop() # a,b 순서 주의
        stack.append(b-a)
    elif i =='/':
        a,b = stack.pop(),stack.pop()
        stack.append(b/a)
    else:
        stack.append(dic[i])
print(f"{stack[0]:.2f}")
