n1,n2 = map(int,input().split())
myStore = []
money = []

for i in range(n2):
    s1 = list(map(int,input().split()))
    myStore.append(s1)
six = []
one = []
for i in range(n2):
    six.append(myStore[i][0])
    one.append(myStore[i][1])
money.append(min(six) * (n1 //6) + min(one) * (n1 % 6))
money.append(min(one)* n1)
money.append(min(six)*((n1//6)+1))
print(min(money))
