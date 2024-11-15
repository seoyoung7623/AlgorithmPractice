# 2001 파리퇴치 D2
'''
N의 배열안에 M의 파리채로 가장 많은 파리를 죽이는 방법
- 모든 MxM을 탐색?
- 가장 큰수가 정답에 가까운가? x
- 겹치는 부분이 많은데 어떻게 일반화하지

1. 모든 경우를 탐색 but 얼마나 범위를 줄인느냐
NxN 5 MxM 3 3x3
N-M+1 * N-M+1 번 의 경우가 나옴
N-M+1 핵심

모든 경우의 수에 두려워하지 말기

2. 누적합 이용하기

'''
# 모든 경우의 수
T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    answer = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for k in range(M):
                for l in range(M):
                    fly += grid[i+k][j+l]
            answer.append(fly)
    print(f"#{test_case} {max(answer)}")

# 누적합 이용
T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    sumGrid = [[0]*(N+1) for _ in range(N+1)]
    # 중요!! 합의셀은 한칸 오른쪽 아래에서 정의함
    for i in range(1,N+1):
        for j in range(1,N+1):
            sumGrid[i][j] = sumGrid[i-1][j] + sumGrid[i][j-1] - sumGrid[i-1][j-1] + grid[i-1][j-1] # 현재 셀
    maxSum = 0
    for i in range(1,N-M+2):
        for j in range(1,N-M+2):
            totalSum = sumGrid[i+M-1][j+M-1] - sumGrid[i-1][j+M-1] - sumGrid[i+M-1][j-1] + sumGrid[i-1][j-1]
            maxSum = max(totalSum,maxSum)
    print(f"#{test_case} {maxSum}")
