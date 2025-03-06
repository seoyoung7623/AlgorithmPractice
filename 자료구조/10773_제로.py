# S4
import sys
input = sys.stdin.readline
K = int(input())
arr = []
for _ in range(K):
    number = int(input())
    if number == 0:
        arr.pop()
    else:
        arr.append(number)
print(sum(arr))