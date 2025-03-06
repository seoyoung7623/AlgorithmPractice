# S4
'''
스택문제 난의도 하
sys로 입력시간을 줄임
'''
import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    number_str = input()
    if number_str[0] == '1':
        number,value = map(int,number_str.split())
        stack.append(value)
    else:
        number = int(number_str)
        if number == 2:
            if not stack:
                print(-1)
            else:
                print(stack.pop())
        elif number == 3:
            print(len(stack))
        elif number == 4:
            if stack:
                print(0)
            else:
                print(1)
        elif number == 5:
            if not stack:
                print(-1)
            else:
                print(stack[-1])

