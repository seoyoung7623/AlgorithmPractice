# 15655 N과M(6)
# 지정 숫자들의 순열 사전순 중복 불가
N,M = map(int,input().split())
arr = list(map(int,input().split()))
result = []
arr.sort()

def backTrack(start):
    if len(box) == M:
        result.append(list(box))
        return
    for i in range(start,N):
        box.append(arr[i])
        backTrack(i+1)
        box.pop()
    
box = []
backTrack(0)
for lst in result:
    print(*lst)