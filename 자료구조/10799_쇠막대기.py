# 10799 쇠막대기 S2
'''
레이저를 쏘는경우는 바로 앞에 '('가 있어야함 -> 그동안 모든 막대 더하기
끝마침 막대는 +1
'''
arr = input()
stack = []
cnt = 0
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
    else:
        if arr[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)