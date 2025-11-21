k = int(input())
arr = list(input().split())
answer = []
visited = [0] * (10)

def check(a,b,sign):
    if sign == '<':
        return a<b
    else:
        return a>b

def dfs(depth, lst):
    if depth == k+1:
        answer.append(''.join(map(str,lst.copy())))
        return
    for i in range(10):
        if visited[i] == 0:
            if depth == 0 or check(lst[-1],i,arr[depth-1]):
                visited[i] = 1
                lst.append(i)
                dfs(depth+1,lst)
                lst.pop()
                visited[i] = 0

dfs(0,[])
print(max(answer))
print(min(answer))


