# 1946 신입사원 S1
import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    N = int(input())
    cnt = 1
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    arr.sort(key=lambda x:x[0])
    max = arr[0][1]
    for i in range(1,N):
        if arr[i][1] == 1:
            cnt += 1
            break
        if arr[i][1] < max:
            cnt += 1
            max = arr[i][1]
    print(cnt)