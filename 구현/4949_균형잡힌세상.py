# S4
'''
Stack
⚠️ 스택이 비어있어 있지않은 경우도 있음
'''
while True:
    text = input()
    if text == '.':
        break
    stack = []
    for t in text:
        if t == '(':
            stack.append('(')
        elif t == ')':
            if not stack or stack.pop() != '(':
                print('no')
                # end
                break
        elif t == '[':
            stack.append('[')
        elif t == ']':
            if not stack or stack.pop() != '[':
                print('no')
                # end
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')
