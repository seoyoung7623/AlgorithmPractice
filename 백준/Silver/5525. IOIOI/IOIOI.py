import sys
input = sys.stdin.readline

N = int(input())
S = int(input())
arr = input()

stack = [0]

for i in range(2,S):
    # print(arr[i-2:i+1])
    if arr[i-2:i+1] == 'IOI':
        stack.append(stack.pop() + 1)
    elif arr[i-2:i+1] == 'OIO':
        continue
    else:
        stack.append(0)
answer = 0
for s in stack:
    if s >= N:
        answer += s-N+1
print(answer)