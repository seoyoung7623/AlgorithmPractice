# 공유기 설치
import sys
input = sys.stdin.readline
arr = []
N,C = map(int,input().split())
answer = 0
for i in range(N):
    arr.append(int(input()))
arr.sort()

def binary_search(arr,start,end):
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]
        count = 1

        for i in range(1,len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]

        if count >= C:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = arr[-1] - arr[0]
binary_search(arr,start,end)
print(answer)
            