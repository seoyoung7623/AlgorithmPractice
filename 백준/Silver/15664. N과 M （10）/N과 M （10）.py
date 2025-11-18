N,M = map(int,input().split())
arr = list(map(int,input().split()))
answer = []
arr.sort()

def dfs(start,lst):
    if len(lst) == M:
        if lst in answer:
            return False
        answer.append(list(lst))
        return 
    for i in range(start,len(arr)):
        lst.append(arr[i])
        dfs(i+1,lst)
        lst.pop()
dfs(0,[])
for e in answer:
    print(*e)