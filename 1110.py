num = int(input())
myNum = num
cnt = 0


while 1:
    n1 = num//10
    n2 = num%10
    sum = n1+n2
    num = n2*10 + sum%10
    cnt += 1
    if myNum == num:
        break
print(cnt)
