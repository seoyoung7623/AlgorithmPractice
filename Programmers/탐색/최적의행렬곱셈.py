# 최적의 행렬 곱셈
def solution(matrix_sizes):
    size = len(matrix_sizes)
    dp = [[0]*size for _ in range(size)]
    #이해가 필요한 코드
    for gap in range(1,size):
        for s in range(size - gap): # 시작위치
            e = s+gap #s에서 gep만큼 떨어진 위치 끝나는 위치

            candidate = list()
            for m in range(s,e): #m: 중간
                candidate.append(
                    dp[s][m] + dp[m+1][e] +
                    matrix_sizes[s][0]*matrix_sizes[m][1]*matrix_sizes[e][1]
                )
            dp[s][e] = min(candidate)

    return dp[0][-1]
print(solution([[5,3],[3,10],[10,6]]))