# 9935 문자열 폭발 G4
'''
1. 파이썬은 음수 인덱스를 허용한다.
2. rstrip()를 이용해 입력값의 줄바꿈을 지워줌
'''
import sys
input = sys.stdin.readline
arr = input().rstrip()
ans = input().rstrip()
stack = []

for i in range(len(arr)):
    stack.append(arr[i])
    if ''.join(stack[-(len(ans)):]) == ans:
        # 인덱스 에러가 나지 않는 이유는? 파이썬은 인덱스가 음수값을 허용하기 때문이다.
        for _ in range(len(ans)):
            stack.pop()
if not stack:
    print("FRULA")
else:
    print(''.join(stack))
