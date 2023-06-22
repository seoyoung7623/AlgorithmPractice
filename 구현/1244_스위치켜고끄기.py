#1244 스위치켜고끄기 S4
N = int(input())
list = list(map(int, input().split()))
list.insert(0,0)
memberCnt = int(input())
for i in range(memberCnt):
    gender,num = map(int,input().split())
    j = 1
    if gender == 1:
        while 1:
            list[num*j] = 1 if list[num*j] == 0 else 0
            j+=1
            if j*num > N:
                break
    if gender == 2:
        list[num] = 0 if list[num] == 1 else 1
        while 1:
            if num-j<=0 or num+j > N:
                break
            if list[num-j] == list[num+j]:
                list[num-j] = 0 if list[num-j] == 1 else 1
                list[num+j] = 0 if list[num+j] == 1 else 1
                j += 1
            else:
                break

for i in range(1, N+1):
    print(list[i], end=' ')
    if i % 20 == 0:
        print()

