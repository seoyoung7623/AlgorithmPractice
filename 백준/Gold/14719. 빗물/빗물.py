import sys
input = sys.stdin.readline

H,W = map(int,input().split())
arr = list(map(int,input().split()))

right_height = [0]*W
left_height = [0]*W
left_height[0] = arr[0]
right_height[-1] = arr[-1]

for i in range(1,W):
    left_height[i] = max(left_height[i-1],arr[i])
for i in range(W-2,-1,-1):
    right_height[i] = max(right_height[i+1],arr[i])
# print(left_height)
# print(right_height)

answer = 0
for i in range(W):
    answer += min(left_height[i],right_height[i])-arr[i]

print(answer)
    
