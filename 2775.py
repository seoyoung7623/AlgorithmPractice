#2775 부녀화장이 될테야
cnt = int(input())

for i in range(cnt):
    memlist = [i+1 for i in range(14)]
    k = int(input())
    n = int(input())
    if k ==0:
        print(memlist[n])
    for a in range(k):
        sum = 0
        for b in range(14):
            sum += memlist[b]
            memlist[b] = sum
    print(memlist[n-1])

            
