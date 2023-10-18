# 15663 N과M(9)
# 중복되는 순열을 여러번 출력하면 안됨
# 중복된 순열 마지막 값을 기억해두었다가 반복하지 않도록 처리
N,M = map(int,input().split())
arr = list(map(int,input().split()))
result = []
arr.sort()

def backTrack(lst):
    if len(lst) == M:
        # if lst in result: # 시간초과
        #     return
        result.append(list(lst))
        return
    remember = 0
    for i in range(N):
        if not visited[i] and arr[i] != remember: #append하는 수가 전에와 같은 수라면 중복되기 때문이다.
            visited[i] = True
            lst.append(arr[i])
            remember = arr[i]
            backTrack(lst)
            lst.pop()
            visited[i] = False
            
    
visited = [False]*N
backTrack([])
for lst in result:
    print(*lst)