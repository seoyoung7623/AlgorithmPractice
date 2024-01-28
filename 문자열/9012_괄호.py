#9012 괄호 S4
'''
스택이용 경우의 수 판단
1. ')'로 끝나는 경우
2. '('로 끝나는 경우

1-1. ')'로 끝났는데 스택이 있는 경우 o pop가능
1-2. ')'로 끝났는데 스택이 없는 경우 x
2-1. 문자열을 다 돌았는데 스택이 있는 경우 x
2-2. 문자열을 다 돌았는데 스택이 없는 경우 o
'''
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