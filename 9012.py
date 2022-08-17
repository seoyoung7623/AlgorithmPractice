#9012 괄호 스택이용 맞았음~ 풀이는 조금 틀림
from inspect import stack

num = int(input())

for n in range(num):
    str = list(input())
    stack = []
    for i in str:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else: #else?
        if not stack:
            print("YES")
        else:
            print("NO")
 
 
    #     if ('(' in stack ) and (')' in stack) and stack[stack.index(')')-1]=='(':
    #         stack.pop()
    #         stack.pop()
    # if not stack:
    #     print("YES")
    # else:
    #     print("NO")