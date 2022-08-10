#폴리오미노
strList = list(input())
xCnt = 0
strList.append(' ')

for i in range(len(strList)):
    if strList[i] == 'X':
        xCnt +=1
    else:
        for j in range(xCnt):
            if xCnt % 4 == 0:
                strList[i-(xCnt-j)] = 'A'
            elif xCnt % 4 == 2:
                strList[i-(xCnt-j)] = 'A'
                strList[i-2] = 'B'
                strList[i-1] = 'B'
            else:
                strList = [-1]
        xCnt = 0
       

for i in strList:
    print(i,end='')


