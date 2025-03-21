# G5
'''
DP
LCS 부분수열에서는 DP로 접근했었음
이번에는 연속 부분수열만 가능

이 문제에서 출력이 길이만 출력하므로 문자열를 저장하지 않고 길이만 저장해도됨
'''
# str1 = input()
# str2 = input()
# length1 = len(str1)
# length2 = len(str2)

# dp = [[0]*(length2+1) for _ in range(length1+1)]
# max_length = 0

# for i in range(1,length1+1):
#     for j in range(1,length2+1):
#         if str1[i-1] == str2[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         dp[i][j] = max(dp[i][j],dp[i-1][j])
# print(max(dp[length1]))
'''
이 답의 오류: 최대값이 length1번째 줄이 아닐수있음
엥 이것도 틀리네 원인: dp[i][j] = max(dp[i][j],dp[i-1][j])의 필요성
'''

# str1 = input().rstrip()
# str2 = input().rstrip()
# length1 = len(str1)
# length2 = len(str2)

# dp = [[0]*(length2+1) for _ in range(length1+1)]
# max_length = 0

# for i in range(1,length1+1):
#     for j in range(1,length2+1):
#         if str1[i-1] == str2[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         # dp[i][j] = max(dp[i][j],dp[i-1][j]) # 이 부분은 LCS 문제에서 사용하는 로직
#         # 공통 부분 문자열을 찾아야하기 때문에 이 부분이 필요하지 않다.
#         # 현재 문자들이 일치할때만 업데이트 되며 아닐경우 업데이트 할 필요없음
# print(max(map(max,dp)))


'''
메모리를 줄인 정답 코드 -> 시간초과가 남..ㅠㅠDP를 2차원으로 저장해서 그런듯?'
'''
# import sys
# input = sys.stdin.readline
# str1 = input().rstrip()
# str2 = input().rstrip()
# length1 = len(str1)
# length2 = len(str2)

# dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
# max_length = 0  # 최장 공통 부분 문자열 길이 저장

# for i in range(1, length1 + 1):
#     for j in range(1, length2 + 1):
#         if str1[i - 1] == str2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#             max_length = max(max_length, dp[i][j])

# print(max_length)
'''
다시 해결책 DP를 이전행과 현재행만 저장하자.
'''
import sys
input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()
length1 = len(str1)
length2 = len(str2)

prev_dp = [0]* (length2+1)
curr_dp = [0]* (length2+1)
max_length = 0

for i in range(1,length1+1):
    for j in range(1,length2+1):
        if str1[i-1] == str2[j-1]:
            curr_dp[j] = prev_dp[j-1] + 1
            max_length = max(curr_dp[j],max_length)
        else:
            curr_dp[j] = 0 # 같은 문자가 아니면 0으로 초기화⭐️
    
    prev_dp,curr_dp = curr_dp,prev_dp
print(max_length)