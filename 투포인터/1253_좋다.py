# 1253 좋다 G4
'''
투포인트
두 수의 합을 구하는 문제이므로 target보다 작은 수 2개를 생각했다.
하지만 문제에서 음수도 가능하기때문에 target의 큰수 작은수를 모두 생각해야함 주의하자
'''
N = int(input())
arr = list(map(int,input().split()))
arr.sort()
count = 0
for i in range(N):
    target = arr[i]
    left,right = 0,N-1
    while left<right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        total = arr[left] + arr[right]
        if  total == target:
            count += 1
            break
        elif total>target:
            right -= 1
        elif total<target:
            left += 1
print(count)
