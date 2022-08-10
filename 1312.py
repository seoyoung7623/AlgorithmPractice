#소수 표기 한글자씩 /손으로 나눗셋 계산하는 방법이용
a,b,n = map(int,input().split())

for i in range(n):
    a = a%b*10
print(a//b)

# c = a/b
# for i in range(n):
#     c = c * 10
# print(int(c%10))