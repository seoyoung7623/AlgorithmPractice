# N과 M3
# 증가하는수 중복 허용 & 같은 순열 중복 허용
N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
result = []

def backTrack(lst):
    if len(lst) == M:
        result.append(list(lst))
        return
    for i in range(N):
        lst.append(arr[i])
        backTrack(lst)
        lst.pop()

backTrack([])
for i in result:
    print(*i)

