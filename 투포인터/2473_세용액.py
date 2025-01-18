# 2473 세용액 G3
'''
3개 포인트 방법
1개는 고정하고 2개를 투포인터로 진행
여기서 투포인트는 처음부터가 아님. 고정값 다음부터 진행해서 중복문제 해결
51퍼에서 시간초과..ㅠㅠ
파이썬으로 하면 다 시간초과나서 pypy로 진행
'''
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
arr.sort()

checking = float('inf')

for i in range(N-2):
    stand = arr[i]
    left = i+1
    right = N-1 
    while left<right:
        total = stand + arr[left] + arr[right]
        if checking > abs(total):
            checking = abs(total)
            answer = [stand,arr[left],arr[right]]

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            print(stand,arr[left],arr[right])
            sys.exit()

print(*answer)