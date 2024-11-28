# 정수 삼각형
'''
가장 합이 큰 트리
'''
def solution(triangle):
    answer = 0
    dp = triangle[:]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i][j] + triangle[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = dp[i][j] + triangle[i-1][j-1]
            else:
                dp[i][j] = dp[i][j] + max(triangle[i-1][j],triangle[i-1][j-1])
    answer = max(dp[-1])
    return answer
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))