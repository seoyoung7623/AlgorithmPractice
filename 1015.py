#1015 해결
num = int(input())

n = list(map(int,input().split()))
result = []
for i in range(num):
    result.append(0)

for i in range(len(n)):
    result[n.index(min(n))] = i
    n[n.index(min(n))] = max(n)+1
#min의 인덱스는 가장 왼쪽에 있는 최소 인덱스로 반환한다.

for i in result:
    print(i,end=' ')

