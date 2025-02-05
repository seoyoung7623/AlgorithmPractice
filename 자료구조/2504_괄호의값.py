# 2504 괄호의 값 G5
'''
리스트의 값이 숫자인지 확인하는 법: isinstance(숫자,int) / isinstance(숫자,(int,float))
괄호가 맞지 않은경우도 고려하기 때문제 🔥 에러처리가 필요하다!
'''
import sys
arr = list(input())
stack = []

def parentheses(i,point,op):
    if not stack: # 🔥 에러처리
        print(0)
        sys.exit()
    if arr[i-1] == op:
        stack.pop()
        stack.append(point)
    else:
        total = 0
        while stack: # 🔥 에러처리
            if stack[-1] == op:
                stack.pop()
                stack.append(total*point)
                break
            elif isinstance(stack[-1],int):
                total += stack.pop()
            else: # 🔥 에러처리
                print(0)
                sys.exit()
        else: # 🔥 에러처리 
            print(0)
            sys.exit()
                

for i in range(len(arr)):
    if arr[i] == '(' or arr[i] == '[':
        stack.append(arr[i])
    elif arr[i] == ')':
        parentheses(i,2,'(')
    elif arr[i] == ']':
        parentheses(i,3,'[')

# 특정요소가 있는지 확인할 때
'''
if '(' or ')' or '[' or ']' in stack:
문자열은 빈 문자열이 아니면 무조건 True를 반환한다.
'''
if set(stack) & {'(', ')', '[', ']'}: # & 교집합 이용!! # 🔥 에러처리
    print(0)
else:
    print(sum(stack))