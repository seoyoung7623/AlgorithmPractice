T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = input().strip()
    stack = []
    for n in N:
        if n == '(':
            stack.append(n)
        elif n == '{':
            stack.append(n)
        elif n == ')':
            if stack and stack[-1] == '(':
	            stack.pop()
            else:
                stack.append(n)
        elif n == '}':
            if stack and stack[-1] == '{':
            	stack.pop()
            else:
                stack.append(n)
    if stack:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} 1")