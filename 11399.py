#11399 ATM 
n = int(input())
numli = list(map(int,input().split()))

numli.sort()
sum = 0
for i in range(len(numli)):
    sum += numli[i]*(n-i) 
print(sum)