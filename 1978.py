#소수 찾기
cnt = 0

num = int(input())
numbers = map(int,input().split())

for n in numbers:
    a = 0
    for i in range(1,n+1):
        if n % i == 0:
            a += 1
    if a <= 2 and n != 1:
        cnt +=1

print(cnt)
