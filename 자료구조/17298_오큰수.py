# G4 https://www.acmicpc.net/problem/17298
'''
내 풀이: DP
불가능: 현재 풀이 오른쪽 값하나만 비교하기 때문에 처리 불가능
'''
# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int,input().split()))
# answer = [-1] * N
# for i in range(N-2,-1,-1):
#     if arr[i] < arr[i+1]:
#         answer[i] = arr[i+1]
#     elif arr[i] >= arr[i+1]:
#         if arr[i] < answer[i+1]:
#             answer[i] = answer[i+1]

# print(*answer)
        
'''
✅ 스택
뒤에서 부터 현재까지 본 수중 큰수들만 남긴다.
while 문이 O(N^2)가 아닌 이유
스택의 값이 한번만 들어가고 한번만 나기기때문에 이중반복문이 아님!
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
stack = []
answer = [-1] * N
for i in range(N-1,-1,-1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1]
    stack.append(arr[i])
print(*answer)
