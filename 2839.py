#n = int(input())

# dp = [-1,-1,-1,1,-1,1]

# for i in range(6,n+1):
#     if dp[i-3] 
#     dp[i] = min(dp[i-3]+1,dp[i-5]+1)
# minlist = []
# while n>0:
#     if n % 3 == 0:
#         cnt+=(n//3)
#         minlist.append(cnt)
#         cnt = 0
#     n = n-5
#     if n<0:
#         break
#     elif n == 0:
#         cnt +=1
#         minlist.append(cnt)
#     else:
#         cnt+=1

# if min(minlist) == 0:
#     print(-1)
# else:
#     print(min(minlist))
n = int(input())
cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += (n//5)
        print(cnt)
        break
    n -= 3
    cnt+=1
else:
    print(-1)

# cnt = 0
# if (n%5)%3 == 0:
#     cnt += n//5
#     cnt += (n%5)//3
#     print(cnt)
#     minList.append(cnt)
#     cnt = 0
# elif n%3 == 0:
#     cnt += n//3
#     print(cnt)
# else:
#     print(-1)
 