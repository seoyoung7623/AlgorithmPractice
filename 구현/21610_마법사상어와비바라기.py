# 21610 마법사 상어와 비바라기 G5
'''
1.이동
2.비내기고 사라지기
3.대각선 물복사버그
4.구름생성

if [i,j] in {리스트}: 리스트로 변수 확인 시 시간초과 주의!!
리스트안에 값이 있으면 넘어가는것을 구현하기 위해서는 리스트를 set으로 변경해 시간 복잡도를 O(1)으로 줄일 수 있다.
cloud_set = set(map(tuple, cloud)) -> 리스트를 집합으로
'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
test_case = []
for _ in range(M):
    d,s = map(int,input().split())
    test_case.append((d,s))

def move(d,s,cloud):
    direction = [(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    answer = []
    for x,y in cloud:
        cx = (x + (direction[d][0]*s))%N
        cy = (y + (direction[d][1]*s))%N
        answer.append([cx,cy])
    return answer

for d,s in test_case:
    cloud = move(d,s,cloud)
    cloud_set = set(map(tuple, cloud))

    # 비내리고 사라지기
    for cx,cy in cloud:
        grid[cx][cy] += 1
    
    # 물복사버그
    for cx,cy in cloud:
        direction = [(-1,-1),(-1,1),(1,-1),(1,1)]
        for dx,dy in direction:
            x = cx+dx
            y = cy+dy
            if 0<=x<N and 0<=y<N and grid[x][y] !=0:
                grid[cx][cy] += 1
    # 구름 생성
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if (i,j) in cloud_set:
                continue
            if grid[i][j] >= 2:
                grid[i][j] -= 2
                new_cloud.append([i,j])
    cloud = new_cloud

answer = 0
for i in range(N):
    for j in range(N):
        answer += grid[i][j]
print(answer)



