# 네트워크 1트
'''
1. visited 사용
2. DFS 사용
'''
def solution(n, computers):
    answer = 0
    visited = [0] * (n)
    def DFS(idx,cnt):
        for j in range(n):
            if idx == j:
                continue
            if computers[idx][j] == 1 and visited[j] == 0:
                visited[j] = cnt
                DFS(j,cnt)
    
    cnt = 1
    for i in range(n):
        if visited[i] == 0:
            visited[i] = cnt
            DFS(i,cnt)
            cnt += 1

    return max(visited)
print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))