# 10989 수 정렬하기 3 B1
# 계수 정렬
import sys
input = sys.stdin.readline
N = int(input())
lst = [0] *10001
for i in range(N):
    num = int(input())
    lst[num] += 1
for i in range(len(lst)):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i,end='\n')