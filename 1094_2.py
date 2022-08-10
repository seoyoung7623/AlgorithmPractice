num = int(input())

list = [64,32,16,8,4,2,1]
cnt = 0

for i in list:
    if num >= i:
        cnt +=1
        num -= i
    
    if num == 0:
        break
print(cnt)