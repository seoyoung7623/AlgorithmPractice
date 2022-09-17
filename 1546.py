#1546 평균
num = int(input())
scorelist = list(map(int,input().split()))
bestScore = max(scorelist)
sum = 0
for i in range(len(scorelist)):
    scorelist[i] = scorelist[i]/bestScore*100
    sum +=scorelist[i]
print(sum/len(scorelist))
