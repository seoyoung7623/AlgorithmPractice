# 1940 주몽 S4
N = int(input())
M = int(input())
arr = list(map(int,input().split()))
arr.sort()

count = 0
left = 0
right = N-1
while left<right:
    total = arr[left] + arr[right]
    if total < M:
        left += 1
    elif total > M:
        right -= 1
    elif total == M:
        count += 1
        left += 1

print(count)