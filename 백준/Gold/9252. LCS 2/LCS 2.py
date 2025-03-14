str1 = input()
str2 = input()

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