n1 = int(input())
n2 = int(input())

n1 = (int(n1/100))*100
while 1:
    if n1%n2==0:
        print(f"{int(n1%100):02}")
        break
    else:
        n1 += 1

