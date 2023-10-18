# 15652 N과 M(4) S3
# 증가하는수 중복 허용 & 같은 순열 중복 불가
N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
result = []

def backtrack(start,lst):
    if len(lst) == M: # 종료조건
        result.append(list(lst))
        return
    for i in range(start,len(arr)):
        lst.append(arr[i])
        backtrack(i,lst) # 중복허용이기때문에 현재 위치부터 다시 파악
        lst.pop()

backtrack(0,[])
for i in result:
    print(*i)
