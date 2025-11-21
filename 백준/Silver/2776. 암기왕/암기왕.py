import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())
for t in range(T):
    a = int(input())
    a_arr = list(map(int,input().split()))
    b = int(input())
    b_arr = list(map(int,input().split()))

    a_arr.sort()
    for i in range(b):
        idx = bisect_left(a_arr,b_arr[i])
        if idx < a and a_arr[idx] == b_arr[i]:
            print(1)
        else:
            print(0)