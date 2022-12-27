#1051 숫자 정사각형

N, M = map(int,input().split())
numList = [list(map(int,input())) for _ in range(N)]

for i in numList:
    print(i)

answer = 0
minSet = min(N,M)
for i in range(N):
    for j in range(M):
        for k in range(minSet):
            if ((i + k) < N) and ((j+k)< M) and (numList[i][j] == numList[i+k][j] == numList[i][j+k] == numList[i+k][j+k]):
                answer = max(answer , (k+1)**2)
print(answer)
            
