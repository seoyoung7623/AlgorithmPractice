# 2470 두 용액 G5
N = int(input())
arr = list(map(int,input().split()))
arr.sort()

left = 0
right = N-1
checking = float('inf')
answer = ()

while left<right:
    total = arr[left] + arr[right]
    if abs(total) < checking:
        answer = (arr[left], arr[right])
        checking = abs(total)

    if total < 0:
        left += 1
    elif total > 0:
        right -= 1
    else:
        print(arr[left], arr[right])
        break
print(*answer)