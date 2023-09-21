# 15652 N과 M(4) S3
N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
result = []

def backtrack(start,lst):
    if len(lst) == M: # 종료조건
        result.append(list(lst))
        return
    for i in range(start,len(arr)):
        lst.append(arr[i])
        backtrack(i,lst)
        lst.pop()

backtrack(0,[])
for i in result:
    print(*i)
