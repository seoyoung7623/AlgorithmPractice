# 게리맨더링 2 G3
'''
고려할점: 선거구 5번의 경우 경계선안에 있기에 내부 채우는것을 주의한다.
완전탐색하여 선거 경계선을 정하고 인원수를 구한다. 범위 주의
'''
import sys
input = sys.stdin.readline
N = int(input())
grid = [[0]+list(map(int,input().split())) for _ in range(N)]
grid.insert(0,[0]*(N+1))
answer = 1e9

for x in range(1,N+1):
    for y in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if x+d1+d2>N or y-d1<1 or y+d2>N:
                    continue
                district = [[0]*(N+1) for _ in range(N+1)]
                for i in range(d1+1):
                    district[x+i][y-i] = 5 #1번 경계
                    district[x+d2+i][y+d2-i] = 5 #4번 경계
                for i in range(d2+1):
                    district[x+i][y+i] = 5 #2번 경계
                    district[x+d1+i][y-d1+i] = 5 #3번 경계
                
                for r in range(x+1,x+d1+d2):
                    fill = False
                    for c in range(1,N+1):
                        if district[r][c]==5:
                            fill = not fill # 한번더 만날때까지 안을 채움
                        if fill:
                            district[r][c] = 5

                # 인구계산
                '''
                1번 선거구 1<=r<x+d1, 1<=c<=y
                2번 선거구 1<=r<x+d2, y<c<=N
                3번 선거구 x+d1<=r<=N, 1<=c<y-d1+d2
                4번 선거구 x+d2<r<N, y-d1+d2<=c<=N
                '''
                population = [0] * 6
                for r in range(1,N+1):
                    for c in range(1,N+1):
                        if district[r][c] == 5: #5선거구
                            population[5] += grid[r][c]
                        elif r<x+d1 and c<=y: #1선거구
                            population[1] += grid[r][c]
                        elif r<=x+d2 and y<c: #2선거구
                            population[2] += grid[r][c]
                        elif x+d1<=r and c<y-d1+d2:#3선거구
                            population[3] += grid[r][c]
                        elif x+d2<r and y-d1+d2<=c: #4선거구
                            population[4] += grid[r][c]
                max_pop = max(population[1:])
                min_pop = min(population[1:])
                answer = min(answer,max_pop-min_pop)
print(answer)