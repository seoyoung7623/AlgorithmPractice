# 2512 예산 S2
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
M = int(input())
lst.sort()
answer = 0

def binary_search(arr,start,end):
    while start <= end:
        mid = (start+end)//2
        arr = lst.copy()
        for i in range(N):
            if arr[i] > mid:
                arr[i] = mid
        if sum(arr) <= M: #sum이 m보다 작을 수 있기때문에 answer을 여가서 처리해줌
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid -1

binary_search(lst,1,lst[-1])
print(answer)
