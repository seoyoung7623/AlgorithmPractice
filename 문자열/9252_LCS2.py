# G4
'''
LCS
DP 최장 공통부분 문자열을 저장한다.
'''
from itertools import combinations
import sys
str1 = input()
str2 = input()

# 나의 접근 조합
# length = min(len(str1),len(str2))
# # str1이 작은 길이
# if len(str1) != length:
#     str1,str2 = str2,str1


# for i in range(length,-1,-1):
#     per1 = combinations(str1,i)
#     per2 = combinations(str2,i)
#     # print(*per2)
#     for p in per1:
#         if p in per2:
#             print(i)
#             print(''.join(p))
#             sys.exit()
# else:
#     print(0)

# DP접근
def lcs(str1,str2):
    len1,len2 = len(str1),len(str2)
    dp = [['']*(len2+1) for _ in range(len1+1)]

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + str1[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1],key=len)
    
    return dp[len1][len2]

result = lcs(str1,str2)
print(len(result))
print(''.join(result))
