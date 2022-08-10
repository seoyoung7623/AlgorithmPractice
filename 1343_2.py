#파이썬에서의 replace()함수는 왼쪽부터 해당하는 문자열을 찾아서 치환해주는 함수이다.

str = input()

str = str.replace("XXXX","AAAA")
str = str.replace("XX","BB")

if 'X' in str:
    print(-1)
else:
    print(str)

# strList = list(input())
# xCnt = 0

# for i in range(len(strList)):
#     if strList[i] == 'X':
#         strList[i] = 'A' 