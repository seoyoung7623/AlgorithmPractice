# 15656 N과M(7) S3
N,M = map(int,input().split())
arr = list(map(int,input().split()))
result = []
arr.sort()

def backTrack(lst):
    if len(lst) == M:
        result.append(list(lst))
        return
    for i in range(N):
        lst.append(arr[i])
        backTrack(lst)
        lst.pop()

backTrack([])
for lst in result:
    print(*lst)