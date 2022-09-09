#2798 블랙잭
n, m = map(int,input().split())

numlist = list(map(int,input().split()))
numlist.sort()
sum = 0
cntlist=[]

for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = numlist[i]+numlist[j]+numlist[k]
            if sum<= m:
                cntlist.append(sum)
            else:
                continue
print(max(cntlist))