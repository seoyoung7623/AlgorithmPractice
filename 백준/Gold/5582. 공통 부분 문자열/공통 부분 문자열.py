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
            curr_dp[j] = 0 # 같은 문자가 아니면 0으로 초기화
    
    prev_dp,curr_dp = curr_dp,prev_dp
print(max_length)