#2609 최대공약수와 최소공배수
n1,n2 = map(int,input().split())
myMin = 0
myMax = 0
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        myMin = i
myMax = max(n1,n2)
while 1:
    myMax +=1
    if myMax%n1 == 0 and myMax%n2 ==0:
        break
print(myMin)
print(myMax)