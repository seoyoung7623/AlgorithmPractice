# 2231 분해합
n = int(input())

for i in range(1,n+1):
    num = list(map(int,str(i)))
    if i+sum(num) == n:
        print(i)
        break
else:
    print(0)