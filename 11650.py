#11650 좌표정렬하기
num = int(input())
numlist = []
for c in range(num):
    setnum = list(map(int,input().split()))
    numlist.append(setnum)
numlist.sort(key=lambda x:(x[0],x[1]))
for i in range(len(numlist)):
    print(numlist[i][0],numlist[i][1])