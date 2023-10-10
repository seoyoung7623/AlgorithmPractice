# 15654 N과M(5)
N,M = map(int,input().split())
arr = list(map(int,input().split()))
answer = []

def backtracking(start):
    if start == M:
        answer.append(list(box))
        return
    for i in range(N):
        if arr[i] in box: # box에 있는것을 continue한다면 정렬을 지킬수있음
            continue
        box.append(arr[i])
        backtracking(start+1)
        box.pop()
arr.sort()
box = []
backtracking(0)
for i in answer:
    print(*i)  
