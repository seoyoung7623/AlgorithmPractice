# 16938 캠프준비 G5
import sys
input = sys.stdin.readline
N,L,R,X = map(int,input().split())
arr = map(int,input().split())
arr = sorted(arr)
answer = 0

def backtrack(start,lst):
    global answer
    if sum(lst) > R:
        return
    elif sum(lst) >= L and len(lst)>=2:
        first, end = lst[0],lst[-1]
        if end - first >= X:
            answer += 1
    for i in range(start,N):
        lst.append(arr[i])
        backtrack(i+1,lst)
        lst.pop()
backtrack(0,[])
print(answer)

