# G5
'''
회전하는 방법
0,N-1
1,N-2

레이어 마다 각각의 배열을 만들어서 회전후 다시 리스트에 저장
'''
from collections import deque

N,M,R = map(int,input().split()) #새로, 가로, 회전 수
grid = [list(map(int,input().split())) for _ in range(N)]

layers = min(N,M) // 2

# 테두리 원소 추출
for layer in range(layers):
    q = deque()
    # top
    for i in range(layer,M-layer):
        q.append(grid[layer][i])
    # right
    for i in range(layer+1,N-layer-1):
        q.append(grid[i][M-layer-1])
    # bottom
    for i in range(M-layer-1,layer-1,-1):
        q.append(grid[N-layer-1][i])
    # left
    for i in range(N-layer-2,layer,-1):
        q.append(grid[i][layer])
    
    q.rotate(-R)

    for i in range(layer,M-layer):
        grid[layer][i] = q.popleft()
    for i in range(layer+1,N-layer-1):
        grid[i][M-layer-1] = q.popleft()
    for i in range(M-layer-1,layer-1,-1):
        grid[N-layer-1][i] = q.popleft()
    for i in range(N-layer-2,layer,-1):
        grid[i][layer] = q.popleft()
    
for i in range(N):
    print(*grid[i])