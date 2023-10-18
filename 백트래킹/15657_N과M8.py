# 15657 N과M(8) S3
# 백트래킹
N,M = map(int,input().split())
arr = list(map(int,input().split()))
result = []
arr.sort()

def backTrack(start,lst):
    if len(lst) == M:
        result.append(list(lst))
        return
    for i in range(start,N):
        lst.append(arr[i])
        backTrack(i,lst)
        lst.pop()
backTrack(0,[])
for lst in result:
    print(*lst)