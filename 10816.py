#10816 숫자카드2
n = int(input())
nlist = list(map(int,input().split()))
m = int(input())
mlist = list(map(int,input().split()))
cnt = 0
cntlist = [0 for _ in range(len(mlist))]

nlist.sort()

# for i in range(len(mlist)):
#     cntlist[i] = nlist.count(mlist[i])
# for i in cntlist:
#     print(i,end= ' ')


start = 0
end = len(nlist) -1

for i in range(len(mlist)):
    min = (start+end)//2
    if mlist[i] == nlist[min]:
        

#    while start <= end:
        


