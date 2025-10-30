T = int(input())

for test_case in range(1, T + 1):
    arr = input().strip().split()
    arr = arr[:len(arr)-1]
    stack = []
    valid = True
    
    for n in arr:
        if n.isdigit(): # 숫자 삽입
            stack.append(n)
        else:
            if len(stack) < 2:
                valid = False
                break
            a = int(stack.pop())
            b = int(stack.pop())
            if n == '+':
                stack.append(a+b)
            elif n == '-':
                stack.append(b-a)
            elif n == '*':
                stack.append(a*b)
            elif n == '/':
                stack.append(b//a)
    
    if len(stack) > 1:
        valid = False
        
    if not valid:
        print(f"#{test_case} error")
    else:
        print(f"#{test_case} {stack[-1]}")
            
            
    
    